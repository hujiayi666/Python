import matplotlib.pyplot as plt

# Data for SWOT analysis
strengths = ["热爱动物", "高需求", "多样化的工作环境", "专业技能"]
weaknesses = ["高压力", "长时间工作", "高成本的教育", "情感压力"]
opportunities = ["职业发展", "科技进步", "市场需求增长", "教育和培训"]
threats = ["竞争激烈", "工作风险", "经济波动", "职业倦怠"]

# Create subplots
fig, ax = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('SWOT Analysis: 是否选择成为兽医', fontsize=16)

# Strengths
ax[0, 0].set_title('优势 (Strengths)')
ax[0, 0].axis('off')
ax[0, 0].text(0.5, 0.5, "\n".join(strengths), fontsize=12, ha='center', va='center', bbox=dict(facecolor='lightgreen', alpha=0.5))

# Weaknesses
ax[0, 1].set_title('劣势 (Weaknesses)')
ax[0, 1].axis('off')
ax[0, 1].text(0.5, 0.5, "\n".join(weaknesses), fontsize=12, ha='center', va='center', bbox=dict(facecolor='lightcoral', alpha=0.5))

# Opportunities
ax[1, 0].set_title('机会 (Opportunities)')
ax[1, 0].axis('off')
ax[1, 0].text(0.5, 0.5, "\n".join(opportunities), fontsize=12, ha='center', va='center', bbox=dict(facecolor='lightblue', alpha=0.5))

# Threats
ax[1, 1].set_title('威胁 (Threats)')
ax[1, 1].axis('off')
ax[1, 1].text(0.5, 0.5, "\n".join(threats), fontsize=12, ha='center', va='center', bbox=dict(facecolor='lightyellow', alpha=0.5))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
