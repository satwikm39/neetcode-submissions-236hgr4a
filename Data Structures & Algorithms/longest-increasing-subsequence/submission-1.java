class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] LIS = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            LIS[i] = 1;
        }

        for (int i = nums.length - 1; i >= 0; i--) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] > nums[i]) {
                    LIS[i] = Math.max(LIS[i], 1 + LIS[j]);
                }
            }
        }

        int max = 1;
        for (int n : LIS) {
            if (n > max) {
                max = n;
            }
        }
        return max;
    }
}
