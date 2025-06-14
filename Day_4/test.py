# lists

student_names = ["Ganga", "Swetha","Sreenivasulu","Ramanjanamma"]
student_names.append("new_user")
student_names.remove("Ganga")
print(student_names)
print(student_names[0])
print(student_names[-1])
print(len(student_names))

s3_bucket_lists = ["Ganga_bucket","Swetha_Dev_Bucket","Sreeni_Prod_Bucket"]
s3_bucket_lists.append("Raju_bucket")
print(s3_bucket_lists)
print(len(s3_bucket_lists))

new_list = s3_bucket_lists[0:3]

#concatenate
print(s3_bucket_lists[0]+"__"+ s3_bucket_lists[1])

#Tuple
s3_bucket_lists = ("Ganga_bucket","Swetha_Dev_Bucket","Sreeni_Prod_Bucket")
print(s3_bucket_lists)
print(len(s3_bucket_lists))

#Print the numbers in small to large
numbers = [1,20,15]
numbers.sort()
print(numbers)