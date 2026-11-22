import numpy as np 
#i) it is incorrect because there is more than 2 arrays in the parenthesis. The correct way is 
#ii) a = np.array([0, 0, 0]) - It has 3 elements in a list and a = np.array([[0, 0, 0]]) - It has a list as an element 
array = np.linspace(1, 48, 48).reshape(3, 4, 4)
print(array)

#20
twenty = array[1,0,3]
print(twenty)

#[ 9. 10. 11. 12.] 
firstlayer_secondrow = array[0,2]
print(firstlayer_secondrow)

#[[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]  
thirdlayer = array[2]
print(thirdlayer)

#[[5. 6.] [21. 22.] [37. 38.]]  
a = array[0,1,0:2] 
b = array[1,1,0:2] 
c = array[2,1,0:2]
all_arrays = np.concatenate((a,b,c))
print(all_arrays)

#[[36. 35.] [40. 39.] [44. 43.] [48. 47.]]  
all_arrays2 =array[2, :, 2:][:, ::-1]
print(all_arrays2)

#[[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]  
all_arrays3 = array[:, :, 0][:, ::-1]
print(all_arrays3)

#[[1. 4.] [45. 48.]] 
all_arrays4 = array[[0, 2], [0, 3]][:, [0, 3]]
print(all_arrays4)

#[[25. 26. 27. 28.] [29. 30. 31. 32.] [33. 34. 35. 36.] [37. 38. 39. 40.]] 
top = array[1, 2:4]
bottom = array[2, 0:2]
all_arrays5 = np.concatenate((top, bottom))
print(all_arrays5)
