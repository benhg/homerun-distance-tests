import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp

# load chicago data
wrigley_data = pd.read_csv("data/savant_data-wrigley.csv")
chisox_data = pd.read_csv("data/savant_data-comiskey.csv")
chi_data = pd.concat([wrigley_data, chisox_data])

# load whole league data
all_data = pd.read_csv("data/savant_data.csv")

# summaries
print("There were {} homeruns at wrigley and {} homeruns at comiskey, for a total of {} in Chicago".format(wrigley_data["hit_distance_sc"].count(), chisox_data["hit_distance_sc"].count() ,chi_data["hit_distance_sc"].count()))
print( "Mean distance in Chicago: {}".format( chi_data["hit_distance_sc"].mean() ) )

print("There were {} homeruns in the MLB".format(all_data["hit_distance_sc"].count()))
print("Mean MLB distance: {}".format( all_data["hit_distance_sc"].mean()))


#first, let's make some graphs
plt.hist(all_data["hit_distance_sc"], alpha=0.5, normed=True, label="All")
plt.hist(chi_data["hit_distance_sc"], alpha=0.5, normed=True, label="Chicago")
plt.ylabel("Relative Frequency")
plt.xlabel("Distance")
plt.legend()
#plt.show()

# now, for the main event. KS test.
ks, p_val = ks_2samp(list(chi_data["hit_distance_sc"]), list(all_data["hit_distance_sc"]))
print("KS is {} (p={})".format(ks, p_val))
