#Maggie Borkowski
#final project

library(foreign)
library(car)

#make data frame
df = read.spss("/Users/maggieborkowski/Dropbox/stats/finalproject.sav", to.data.frame=TRUE)
df$Test <- as.factor(df$Test)

#MANOVA
depend <- cbind(df$Reading_Score, df$Reading_Time, df$Math_Score, df$Math_Time)
mresults <- manova(depend ~ df$Gender*df$Test)
summary(mresults, test="Roy")

#factorial ANOVA on each DV
summary.aov(mresults)

#Levene's Test on significant univariate results
leveneTest(df$Reading_Score, df$Gender)
leveneTest(df$Reading_Score, df$Test)
leveneTest(df$Math_Score, df$Gender)

#mean values divided by gender and test for each DV
tapply(df$Reading_Score, list(df$Gender, df$Test), mean)
tapply(df$Reading_Time, list(df$Gender, df$Test), mean)
tapply(df$Math_Score, list(df$Gender, df$Test), mean)
tapply(df$Math_Time, list(df$Gender, df$Test), mean)
