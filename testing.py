import time
# Syncronus Program
# step 1 
# print("Water is begin to boiling")
# time.sleep(5)
# print("water is now boiled")



# # step 2 
# print("Roti Bana na shuru")
# time.sleep(5)
# print("Roti Ban gayi hai")


# Assyncronus Program

import asyncio
# step 1 

async def water_boiling():
    print("Water is begin to boiling")
    await asyncio.sleep(5)
    print("water is now boiled")

water_boiling()

# step 2 
async def Roti_banana():
    print("Roti Bana na shuru")
    await asyncio.sleep(5)
    print("Roti Ban gayi hai")
    
Roti_banana()    