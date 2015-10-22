def main():
    def dot_product(list1, list2):
      vec1 = input("Enter first set of numbers:")
      vec2 = input("Enter first set of numbers:")

      list1 = map(int, list1.split(","))
      list2 = map(int, list2.split(","))

      if len(vec1) < len(vec2) or len(vec1) > len(vec2):
          nonum = float("NaN")
      else:
          nonum = sum([a * b for a,b in zip(list1, list2)])
      return nonum
    print(dot_product(vec1 ,vec2))

if __name__ == "main": main()
