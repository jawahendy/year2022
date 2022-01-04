// Complete the maxSubsetSum function below.
function maxSubsetSum(arr) {

    const N = arr.length
    const maxes = Array(N).fill(0)

    maxes[0] = Math.max(arr[0], 0)
    maxes[1] = Math.max(arr[0], arr[1], 0)
    for (let i = 2; i < N; i++) {
        maxes[i] = Math.max(arr[i], maxes[i - 1], maxes[i - 2] + arr[i], 0)
    }

    return maxes[N - 1]
}
