source("bs_bsm_options_greeks.r")
source("bs_options_pricing.r")
source("mcs_options_pricing.r")

#implementation greeks
#delta
delta("c", S = 105, X = 100, Time = 0.5, r = 0.1, b = 0, sigma = 0.36)
delta("p", S = 105, X = 100, Time = 0.5, r = 0.1, b = 0, sigma = 0.36)
#theta
theta("p", S = 430, X = 405, Time = 1/12, r = 0.07, b = 0.07 - 0.05, sigma = 0.2)
#vega
vega("c", S = 55, X = 60, Time = 0.75, r = 0.1, b = 0.1, sigma = 0.3)


#mcs implementation
#simulate
TypeFlag <<- "c"
S <<- 100
X <<- 100
Time <<- 1/12
sigma <<- 0.4
r <<- 0.1
b <<- 0.1
set.seed = 4711
mc= MonteCarloOption(delta.t = 1/360, pathLength = 30, mcSteps = 5000,
                     mcLoops= 20, path.gen = wienerPath, payoff.calc = plainVanillaPayoff)

#plot
mcPrice = cumsum(mc)/(1:length(mc))
plot(mcPrice, type = "l", main = "Arithmetic Asian Option", xlab = "Monte Carlo Loops",
ylab = "Option Price")
abline(h = 5.0118, col = "red")
grid()

install.packages(c('reticulate', 'data.table', 'readxl'))
repl_python()
library(reticulate)
library(data.table)
library(readxl)
use_condaenv("M2DM")
source_python('D:/blx_mdp/BlxHerokuDash/functions/etl_functions.py')
pd<-import("pandas")
np<-import("numpy")

py_config()
py_run_file("D:/blx_mdp/BlxHerokuDash/etls/pipeline_p50_asset.py")


path_dir_in<-"D:/blx_mdp/cwd/in/"
path_dir_temp<-"D:/blx_mdp/cwd/temp/"

prod<-read_excel(paste(path_dir_in, "template_prod.xlsx", sep =""), sheet="prod")#nolint
prod_pct<-read_excel(paste(path_dir_in, 'template_prod.xlsx', sep =""),sheet="prod_perc")#nolint
mean_pct<-read_excel(paste(path_dir_in, 'template_prod.xlsx', sep=""),sheet="mean_perc")#nolint
data<-read_excel(paste(path_dir_in, 'template_asset.xlsx', sep=""))