    public static int findDigits(int n) {
    // Write your code here
        int count = 0;
    int num = n;
    while (n > 0) {
      int r = n % 10;
      if (r != 0 && num % r == 0) count++;
      n = n / 10;
    }
    return count;

    }