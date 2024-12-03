import matplotlib.pyplot as plt
import numpy as np

# Data for comparison
categories = [
    "Age", "Disability_status", "Gender_identity","Nationality", "Physical_appearance", "Race_ethnicity",
    "Race_x_gender", "Race_x_SES", "Religion", "SES", "Sexual_orientation"
]

# BERT model accuracy (from original data)
bert_accuracies = [
    0.45916666666666667, 0.31613372093023256, 0.45558375634517767, 0.32712082262210795,
    0.4305555555555556, 0.35609318996415773, 0.4532608695652174, 0.4519230769230769,
    0.4198051948051948, 0.3950501253132832, 0.36477433004231313
]

# UnLog model accuracy (from the second data)
unlog_accuracies = [
    0.49166666666666664, 0.5026162790697675, 0.4936548223350254, 0.4569408740359897,
    0.47800925925925924, 0.49874551971326164, 0.49320652173913043, 0.49475524475524474,
    0.5071428571428571, 0.49542606516290727, 0.4652679830747532
]

# Set up the figure and axis for plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Bar positions and width
x = np.arange(len(categories))
width = 0.4  # Bar width

# Plotting the bars for BERT and UnLog models
bars_bert = ax.bar(x - width/2, bert_accuracies, width, label="BERT (baseline)", color='orange')
bars_unlog = ax.bar(x + width/2, unlog_accuracies, width, label="UnLoG (our model)", color='blue')

# Adding labels and title
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('BBQ Accuracy Comparison: BERT vs UnLoG', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)
ax.legend()

# Adding values on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset label
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(bars_bert)
add_labels(bars_unlog)

save_path = "/home/nlpgpu7/ellt/suyun/bbq_accuracy/evaluation/image/BBQ_accuracy_comparison.png"
plt.tight_layout()
plt.savefig(save_path)
print(f"그래프가 저장되었습니다: {save_path}")

##################################################################
#2. 전체
# Data for overall average accuracy comparison
models = ['BERT', 'UnLoG']
average_accuracies = [0.40267884624845307, 0.48885746299589666]

# Set up the figure for plotting
fig, ax = plt.subplots(figsize=(6, 6))

# Plotting the bars for average accuracy of both models
bars = ax.bar(models, average_accuracies, color=['orange', 'blue'])

# Adding labels and title
ax.set_ylabel('Average Accuracy', fontsize=12)
ax.set_title('BBQ Average Accuracy Comparison: BERT vs UnLoG', fontsize=14)

# Adding values on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset label
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(bars)

save_path = "/home/nlpgpu7/ellt/suyun/bbq_accuracy/evaluation/image/total_nolabel_BBQ_accuracy_comparison.png"
plt.tight_layout()
plt.savefig(save_path)
print(f"그래프가 저장되었습니다: {save_path}")
