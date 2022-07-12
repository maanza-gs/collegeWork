library(tidyverse)
library(recommenderlab)

books <- readr::read_csv('Z:/collegeThings/Sem4/R_lab/package/books.csv')  #books
ratings <- readr::read_csv('Z:/collegeThings/Sem4/R_lab/package/ratings.csv') #ranking

rap_matrix <- books %>% 
  select(authors, title) %>% 
  mutate(n = 1) %>% 
  arrange(title) %>% 
  pivot_wider(names_from = "title", values_from = "n", values_fill = list(n = 0)) %>% 
  select(-authors) %>% 
  as.matrix() %>% 
  as("binaryRatingMatrix")


trainingSchema <- evaluate(rap_matrix, method=, type="topNList",n=1:10, parameter=NULL, progress = TRUE, keepModel=FALSE)
training_schema

UBCF_Model <- evaluate(training_schema, method = "UBCF", type = "topNList", n = 5)

IBCF_Model <- evaluate(training_schema, method = "IBCF", type = "topNList", n = 5)

UBCF_Model %>% avg()

IBCF_Model %>% avg() %>% as_tibble()

tune_engines <- function(schema, parameters){
  
  UBCF_Model <- evaluate(schema, method = "UBCF", type = "topNList", n = 5, param = list(nn = parameters))
  IBCF_Model <- evaluate(schema, method = "IBCF", type = "topNList", n = 5, param = list(k = parameters))
  
    UBCF_Model %>% 
    avg() %>% 
    as_tibble() %>% 
    mutate(model = "UBCF") %>% 
    rbind(IBCF_Model %>% 
            avg() %>% 
            as_tibble() %>% 
            mutate(model = "IBCF")) %>% 
    return()
  
  
  
}


tune_grid <- tibble(parameters = c(2, 3, 5, 10, 15, 20, 25))

history <- tune_grid %>% 
  mutate(results = map(parameters, ~tune_engines(training_schema, .x))) %>% 
  unnest()

history %>% 
  ggplot(aes(x = parameters, y = TPR, fill = model, label = parameters)) + geom_col(position = "dodge") + geom_text(aes(x = parameters, y = TPR))


UBCF_Final_model <- Recommender(getData(training_schema, "train"), "UBCF", param = list(nn = 5))

UBCF_Final_model

predictions <- predict(UBCF_Final_model, getData(training_schema, "known"), type = "topNList")
calcPredictionAccuracy(predictions, getData(training_schema,"unknown"), given = -1)

rec_engine <- Recommender(rap_matrix, "UBCF", param = list(nn = 5))
rec_engine

books %>% filter(str_detect(authors, "2Pac")) %>% distinct(title) %>% arrange(title)

#GIVING Songs via which recommendation would be given
andrew_songs <- books %>% 
  select(title) %>% 
  distinct() %>% 
  arrange(title) %>% 
  filter(title %in% c("All Of The Lights", "Alright", "Bitch Don’t Kill My Vibe", "m.A.A.d. city", "Changes")) %>%  
  rbind(books %>% select(title) %>% distinct()) %>% 
  count(title) %>% 
  mutate(n = n -1) %>% 
  pivot_wider(names_from = "title", values_from = "n", values_fill = list(n = 0)) %>% 
  as.matrix() %>% 
  as("binaryRatingMatrix")


rec_engine

predict(rec_engine, andrew_songs) %>% as("list") %>% as.data.frame()