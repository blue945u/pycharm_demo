from my_module import hello_module
from Algorithms.sorts import bubble_sort
from Algorithms.other import two_sum

if __name__ == '__main__':
    demo = hello_module.Demo()
    print("I am ..." + demo.hello_world())

    # print( two_sum.twoSum([1,2,3,4,5,6,7,8,9,11,11,11,11,11,11,11,11,11,11,11,11,12,12,12,12,13,14,15,16,17,18,19,98,109], 100))
    # print(
    # two_sum.twoSum(
    #     [1, 2, 3, 4, 5, 6,
    # 7, 8, 9, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 14, 15, 16, 17,
    # 18, 97, 980, 109],
    #     100))
    # num_list = [1, 2, 3, 4, 5, 6,
    # 7, 8, 9, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 14, 15, 16, 17,
    # 18, 97, 980, 109]
    # target = 200
    # print(two_sum.twoSum(
    # num_list,
    # target))

    # print(bubble_sort.bubble_sort([1, 2, 3, 2, 1]))

    # print(demo.quadratic_formula(2, 1, 0))
    # print(demo.quadratic_formula(2, 4, 0))
    # print(demo.quadratic_formula(2, 2, 2))

    # while True:
    #     a = int(input("a: "))
    #     b = int(input("b: "))
    #     c = int(input("c: "))
    #     result = demo.quadratic_formula(a, b, c)
    #     print(result)
