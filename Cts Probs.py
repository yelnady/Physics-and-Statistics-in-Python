import scipy.stats as st

print(st.norm.cdf(10/3)-st.norm.cdf(5/3)) # P (Z <= 1.57)

print("joe")
print(st.norm.ppf(0.2)) # Inverse