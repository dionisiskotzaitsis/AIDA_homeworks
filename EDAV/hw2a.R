# hw2a

library(tidyverse)
library(statisticalModeling)



# Μελετήστε τη δομή του dataset Birth_weight
head(Birth_weight) 
str(Birth_weight)

# Δώστε ένα διάγραμμα για κάθε ένα από τα παρακάτω:

# Μελετήστε την κατανομή των τιμών της μεταβλητής income

ggplot(data = Birth_weight) + 
  geom_bar(mapping = aes(x = income))


# Μελετήστε την κατανομή των τιμών της μεταβλητής baby_wt

ggplot(data = Birth_weight) + 
  geom_freqpoly(mapping =aes(x=baby_wt))

ggplot(data = Birth_weight) +
  geom_histogram(mapping =aes(x=baby_wt))

ggplot(data = Birth_weight) + 
  geom_density(mapping =aes(x=baby_wt))

# Μελετήστε την κατανομή των τιμών της μεταβλητής mother_age

ggplot(data = Birth_weight) + 
  geom_freqpoly(mapping =aes(x=mother_age))

ggplot(data = Birth_weight) +
  geom_histogram(mapping =aes(x=mother_age))

ggplot(data = Birth_weight) + 
  geom_density(mapping =aes(x=mother_age))

# Μελετήστε τη σχέση ανάμεσα στις μεταβλητές mother_age και income

ggplot(data = Birth_weight)+
  geom_jitter(mapping = aes(x=mother_age,y=income))

ggplot(data = Birth_weight)+
  geom_boxplot(mapping = aes(x=mother_age,y=income))

ggplot(data = Birth_weight)+
  geom_point(mapping = aes(x=mother_age,y=income))

ggplot(data = Birth_weight)+
  geom_smooth(mapping = aes(x=mother_age,y=income))


# Μελετήστε τη σχέση ανάμεσα στις μεταβλητές baby_wt και smoke

ggplot(data = Birth_weight)+
  geom_jitter(mapping = aes(x=smoke,y=baby_wt))

ggplot(data = Birth_weight)+
  geom_boxplot(mapping = aes(x=smoke,y=baby_wt))

ggplot(data = Birth_weight) +
  geom_pointrange(
    mapping = aes(x = smoke, y = baby_wt),
    stat = "summary"
  )


# Μελετήστε τη σχέση ανάμεσα στις μεταβλητές mother_age και mother_wt

ggplot(data=Birth_weight)+
  geom_point(mapping = aes(x=mother_age,y=mother_wt),position="jitter")

ggplot(data=Birth_weight)+
  geom_smooth(mapping = aes(x=mother_age,y=mother_wt))


# Μελετήστε τη σχέση ανάμεσα στις μεταβλητές mother_wt, baby_wt και smoke

ggplot(data=Birth_weight)+
  geom_point(mapping = aes(x=baby_wt,y=mother_wt,color=smoke,shape=smoke),position="jitter")

ggplot(data = Birth_weight) +
  geom_point(mapping = aes(x = baby_wt, y = mother_wt,color=smoke))+
  geom_smooth(se=FALSE,mapping = aes(x = baby_wt, y = mother_wt, group = smoke,linetype=smoke))


ggplot(data = Birth_weight) + 
  geom_smooth(mapping = aes(x = baby_wt, y = mother_wt)) + 
  facet_wrap(~ smoke, nrow = 2)

# Μελετήστε την κατανομή (boxplot) της μεταβλητής baby_wt σε σχέση με τη μεταβλητή smoke

ggplot(data=Birth_weight)+
  geom_boxplot(mapping=aes(x=baby_wt,y=smoke))+
  coord_flip()

# Μελετήστε την κατανομή (boxplot) της μεταβλητής baby_wt σε σχέση με τις μεταβλητές smoke και income

ggplot(data=Birth_weight)+
  geom_boxplot(mapping=aes(x=baby_wt,y=smoke))+
  facet_wrap(~income)+
  coord_flip()


ggplot(data=Birth_weight)+
  geom_boxplot(mapping=aes(x=baby_wt,y=income))+
  facet_wrap(~smoke)

