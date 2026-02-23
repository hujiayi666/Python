#编程实现教材第五章课后习题
scores = {
    "012": [90, 94, 97, 86, 85, 89, 88, 85],
    "005": [91, 91, 92, 98, 90, 96, 90, 95],
    "108": [96, 86, 97, 96, 87, 86, 86, 96],
    "037": [95, 95, 94, 93, 97, 98, 99, 95],
    "066": [95, 87, 94, 94, 93, 99, 96, 97],
    "020": [89, 97, 91, 95, 89, 94, 97, 92]
}
def calculate_avg_score(scores_list):
    sorted_scores = sorted(scores_list)
    return sum(sorted_scores[1:-1]) / (len(sorted_scores) - 2)
results = {}
for key, value in scores.items():
    results[key] = calculate_avg_score(value)
sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
for index, (player_number, score) in enumerate(sorted_results):
    print(f"选手编号：{player_number}，最后得分：{score}")














