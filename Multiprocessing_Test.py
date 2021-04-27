import time
import random
import multiprocessing

#泡沫排序
def Bubble_Sort(arr):
    arr = random.sample(range(1,1000000),1000) #產生不重複亂數
    print('排序前:',arr)
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]      
    return arr
        

def main():
    multiprocessing.freeze_support() # Windows 平台要使用此函數，避免 RuntimeError
    pool = multiprocessing.Pool()
    cpus = multiprocessing.cpu_count() #CPU核心數量
    results = []

    for i in range(cpus):
        result = pool.apply_async(Bubble_Sort, args=(i,)) #異步處理
        results.append(result)

    pool.close() #關閉進程池，不再接受新的進程
    pool.join() #主進程阻塞等待子進程的退出 

    print('\n')
    for result in results:
        print('排序後:',result.get())


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    total_time = end_time - start_time
    print('執行時間:',total_time)
