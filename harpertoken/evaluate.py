def compute_metrics(predictions, references):
    # Word Error Rate (WER) calculation
    wer = calculate_wer(predictions, references)
    cer = calculate_cer(predictions, references)
    return wer, cer


def calculate_wer(predictions, references):
    # Implementation of WER
    # This function calculates the WER based on the predictions and references
    errors = 0
    for i in range(len(predictions)):
        prediction = predictions[i]
        reference = references[i]
        errors += edit_distance(prediction, reference)
    total_words = sum(len(reference.split()) for reference in references)
    return errors / total_words


def calculate_cer(predictions, references):
    # Implementation of CER
    # This function calculates the CER based on the predictions and references
    errors = 0
    total_chars = 0
    for i in range(len(predictions)):
        prediction = predictions[i]
        reference = references[i]
        errors += edit_distance(prediction, reference)
        total_chars += len(reference)
    return errors / total_chars


def edit_distance(prediction, reference):
    m = len(prediction) + 1
    n = len(reference) + 1
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = i
    for j in range(n):
        dp[0][j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if prediction[i - 1] == reference[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[m - 1][n - 1]
