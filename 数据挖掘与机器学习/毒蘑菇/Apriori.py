import itertools
import time
from tqdm import tqdm


# ========== Apriori 算法核心函数 ==========

def createC1(dataSet):
    """生成候选1项集"""
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))


def scanD(D, Ck, minSupport):
    """从候选集中筛选出频繁项集"""
    ssCnt = {}
    for tid in tqdm(D, desc="扫描数据集", leave=False, ncols=80):
        for can in Ck:
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1

    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k):
    """由频繁k项集生成候选(k+1)项集"""
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport=0.5):
    """Apriori主算法"""
    print(f"\n=== 开始Apriori算法，最小支持度={minSupport} ===")
    start_time = time.time()

    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while len(L[k - 2]) > 0:
        print(f"生成候选{k}项集...")
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        if len(Lk) == 0:
            break
        L.append(Lk)
        k += 1

    end_time = time.time()
    print(f"Apriori频繁项集生成完毕，总耗时：{end_time - start_time:.2f} 秒。")
    return L, supportData


# ========== 生成关联规则部分 ==========

def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    """计算置信度"""
    prunedH = []
    for conseq in H:
        if supportData.get(freqSet - conseq, 0) > 0:
            conf = supportData[freqSet] / supportData[freqSet - conseq]
            if conf >= minConf:
                brl.append((freqSet - conseq, conseq, conf))
                prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    """生成候选规则集合"""
    m = len(H[0])
    if len(freqSet) > (m + 1):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if len(Hmp1) > 1:
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)


def generateRules(L, supportData, minConf=0.7):
    """主函数：生成强关联规则"""
    print(f"\n=== 开始生成关联规则，最小置信度={minConf} ===")
    start_time = time.time()

    RuleList = []
    for i in tqdm(range(1, len(L)), desc="生成规则层次", leave=False, ncols=80):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if i > 1:
                rulesFromConseq(freqSet, H1, supportData, RuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, RuleList, minConf)

    end_time = time.time()
    print(f"关联规则生成完毕，总耗时：{end_time - start_time:.2f} 秒。")
    return RuleList


# ========== 数据加载与运行部分 ==========

if __name__ == "__main__":
    # --- 测试数据集 ---
    dataset = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
    L1, supportData1 = apriori(dataset, minSupport=0.5)
    rules1 = generateRules(L1, supportData1, minConf=0.7)

    print("\n=== 简单数据集满足最小支持度0.5、置信度0.7的强关联规则 ===")
    for rule in rules1:
        print(f"{set(rule[0])} --> {set(rule[1])}, conf={rule[2]:.2f}")

    # --- 毒蘑菇数据集 ---
    print("\n=== 开始处理 mushroom.dat 数据集 ===")
    total_start = time.time()

    with open(r"D:\cxdownload\mushroom.dat") as f:
        mush_dataset = [line.strip().split() for line in f.readlines()]

    L2, supportData2 = apriori(mush_dataset, minSupport=0.3)
    rules2 = generateRules(L2, supportData2, minConf=0.7)

    total_end = time.time()
    print(f"\n=== 毒蘑菇数据集 Apriori 完成，总耗时 {total_end - total_start:.2f} 秒 ===")

    # --- 筛选包含“2”的频繁项集与规则 ---
    freq_with_2 = [item for sublist in L2 for item in sublist if '2' in item]
    rules_with_2 = [r for r in rules2 if any('2' in x for x in (r[0] | r[1]))]

    # --- 控制台简要展示 ---
    print(f"\n=== 包含特征值'2'的频繁项集（共 {len(freq_with_2)} 个） ===")
    for i, item in enumerate(freq_with_2[:10], 1):  # 控制台仅显示前10条
        print(f"{i}. {set(item)}  支持度 = {supportData2[item]:.2f}")

    print(f"\n=== 包含特征值'2'的强关联规则（共 {len(rules_with_2)} 条） ===")
    for i, rule in enumerate(rules_with_2[:10], 1):  # 控制台仅显示前10条
        print(f"{i}. {set(rule[0])} --> {set(rule[1])}, conf={rule[2]:.2f}")

    # --- 写入结果文件 ---
    with open("mushroom_results.txt", "w", encoding="utf-8") as f:
        f.write(f"=== 毒蘑菇数据集Apriori结果 ===\n")
        f.write(f"最小支持度: 0.3, 最小置信度: 0.7\n")
        f.write(f"总共生成 {sum(len(x) for x in L2)} 个频繁项集，{len(rules2)} 条规则。\n\n")

        f.write("【包含'2'的频繁项集】\n")
        for item in freq_with_2:
            f.write(f"{set(item)}  支持度={supportData2[item]:.3f}\n")

        f.write("\n【包含'2'的强关联规则】\n")
        for rule in rules_with_2:
            f.write(f"{set(rule[0])} --> {set(rule[1])}, conf={rule[2]:.3f}\n")

    print("\n所有包含'2'的频繁项集与规则已保存到文件：mushroom_results.txt")
