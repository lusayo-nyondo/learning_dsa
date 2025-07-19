void main() {
  List<int> nums = [1, 2, 3, 4, 5, 6, 7, 8];

  List<int> rotated = []..addAll(nums.sublist(3)..addAll(nums.sublist(0, 3)));
  print(rotated);
}
