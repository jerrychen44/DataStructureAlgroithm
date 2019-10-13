/*
https://www.geeksforgeeks.org/bucket-sort-2/
https://www.youtube.com/watch?v=VuXbEb5ywrU

Bucket sort

簡單來說就是一個 array, size n

1.build buckets : O(n*1)
建造一個 size n 的 buckets,
然後把 array 中的值的第一位, 當作 buckets index (有點hash fun 的味道)
所以 bucket_idx = n * array[i] ex: array[i] 是 0.8, 則 buckets_idx = 8
or 其他設計, 總之讓這些 unsorte valu hash到不同的
buckets, 碰撞後就繼續append 在後面


2.
好了之後, 每個buckets 各自sort(用insertion sort), 接著照順序把每個buckets soted 後的結果依照順序擺好
就是sorted array 了
=>This instertion sort also takes O(n) time on average if all numbers are uniformly distributed

total time complexity: O(2n) = O(n)


*/
#include<iostream>
#include<vector>


class Bucket_sort{

public:
    std::vector<int> sort(std::vector<int> &nums);

};


std::vector<int> Bucket_sort::sort(std::vector<int> &nums){

    //int numsize = nums.size();
    int buckets_size = 10;
    // 1) Create n empty 2D buckets
    std::vector<std::vector<int>> buckets(buckets_size);
    // 2) Put array elements in different buckets:
    // time: O(n*1)
    for(int val : nums){
        int bidx = val%buckets_size;
        //std::cout<< "bidx:"<<bidx<<std::endl;
        buckets[bidx].emplace_back(val);
    }
    //std::cout<< "buckets[9]:"<<buckets[9][0]<<std::endl;

    // 3) Sort individual buckets
    // 一次 sort O(logn) * 共 n 次 O(n) = O(nlogn)
    for(int i=0;i<buckets_size;++i)
        std::sort(buckets[i].begin(),buckets[i].end());

    // 4) Concatenate all buckets into arr[]
    std::vector<int> rst;
    for (int i = 0; i < buckets_size; i++)
        for (int j = 0; j < buckets[i].size(); j++)
            rst.emplace_back(buckets[i][j]);
    return rst;
}



int main(){
    Bucket_sort bsort = Bucket_sort();

    std::vector<int> nums{9,3,2,4,5,2,1};
    std::vector<int> rst = bsort.sort(nums);

    for(auto v:rst)
        std::cout<< v << std::endl;



    return 0;
}