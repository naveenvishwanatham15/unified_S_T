#two sum
"""Given an array nums and a target,
return indices of two numbers that add up to target. Each input has exactly one solution."""
import tempfile

numbers =[2,7,11,15]
target = 9
def solution(nums:list,target:int) -> list:
    for i ,k in enumerate(numbers):
        if target-k in numbers:
            return i,numbers.index(target-k)
print(solution(numbers,target))

#anagram
string1="listen"
string2="silent"
print(sorted(string1)==sorted(string2))

#Longest substring without repeating characters

#fast api + pydantic
"""from fastapi import FastAPI,HTTPException,Depends,HTTPException
from pydantic import Basemodel, Field, field_validator, BaseModel
from typing import List ,Optional
import uuid
app=FastAPI(title="example app")

class DrugCheckRequest(BaseModel):
    patient_id:str=  Field(...,min_length=1,description="patient id")
    medications:List[str] = Field(...,min_length=1,description="medications")
    required_human_review:bool = False

    @field_validator(["patient_id","medications","required_human_review"])
    def no_empty_string(cls,v):
        if any(not m.strip() for m in v):
            raise ValueError("medication names cannot be empty")
        return [m.strip() for m in v]

class Interaction(BaseModel):
    drug_a:str
    drug_b:str
    severity : str
    explaination : str

class DrugCheckResponse(BaseModel):
    patient_id:str
    request_id:str
    medications:List[str]
    required_human_review:bool
    confidance:float =Field(...,min_length=1,description="confidance")"""

"""@app.post("/check-interactions",response_model=DrugCheckResponse):
async def check_interactions()"""

a = [1, 2, 3]
b = a[:]
b[0] = 99
print(a, b)

a = {"x": [1, 2]}
b = a.copy()
b["x"].append(3)
print(a)


#Write a function swap_first_last(lst) that swaps the first and last elements in place and returns nothing. Then verify the caller sees the change.

def swap_first_last(lst):
    temp=lst[0]
    lst[0]=lst[-1]
    lst[-1]=temp
    print(lst)
    return lst

print(swap_first_last([1,2,3]))

def swap_first_last(lst):
    lst[0],lst[-1]=lst[-1],lst[0]
    return lst
print(swap_first_last([1,2,3]))
# this is reference not a copy
d=[1,2,3]
b=d
d.append(4)
print(b)

# how to copy data
d=[1,2,3]
b=d[:]
b.append(4)
print(d)

import copy
b=copy.deepcopy(d)
print("copying d into b",b)

a = {"x": [1, 2]}
b = copy.deepcopy(a)
b["x"].append(3)
print(a)



def add_user(name, users=None):
    if users is None:
        users = []
    users[name] = True
    return users


# List vs generator
a = [x*x for x in range(5)]      # [0, 1, 4, 9, 16]   — in memory
b = (x*x for x in range(5))      # <generator object>  — lazy
print(list(b))                   # [0, 1, 4, 9, 16]
print(list(b))
print(b)
s = "banana"
print(s.count("a"))
print(s.upper())
print(s.lower())

s = "madam"
if s==s[::-1]:
    print("its a fucking palindrome")
else:
    print("not a palindrome")
#Count vowels in a string
vowels = ["a","e","i","o","u"]
s = "madam"
count=0
for i in s:
    if i in vowels:
        count+=1
print(count)
#Count how many times a character appears
print(s.count("m"))

#Sum of List
Input=[1, 2, 3, 4, 5]

count=0
for i in Input:
    count+=i
print(count)

#Maximum of List
def maximun(nums):

    maxi=0
    for i in nums:
        if i>maxi:
            maxi=i
    return maxi
print(maximun([3, 7, 1, 9, 4]))

# Count Occurrences
nums = [1, 2, 3, 2, 4, 2]
target = 2
def count(nums,target):
    s=0
    for i in nums:
        if target==i:
            s=s+1
    return s
print(count(nums,target))

#Reverse a List (in place)
Input=[1, 2, 3, 4, 5]
Output= [5, 4, 3, 2, 1]
print(Input[::-1])
#Check if Sorted

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False

    return True
print(is_sorted([1,2,3,4,5]))
#Find Index of Target
nums = [10, 20, 30, 40]
target = 30

def find_index(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
print(find_index(nums,target))

#Remove Duplicates
Input=[1, 2, 1, 3, 2, 4]
Output= [1, 2, 3, 4]
def duplicate(nums):
    dict1={}
    for i in nums:
        if i not in dict1:
            dict1[i]=1
        dict1[i]=dict1[i]+1
    return list(dict1.keys())
print(duplicate(Input))

#Two Sum
nums = [2, 7, 11, 15]
target = 9
