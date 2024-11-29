import os
import json
import argparse
import wandb

"""
python /home/nlpgpu7/ellt/suyun/bbq_accuracy/evaluation/combine_results.py \
    --result_dir /home/nlpgpu7/ellt/suyun/bbq_accuracy/EXP_FOL_bert/bbq \
    --output_file /home/nlpgpu7/ellt/suyun/bbq_accuracy/EXP_FOL_bert/bbq/combined_results.json
"""

def combine_results(result_dir, output_file):
    category_results = []
    total_accuracy = 0.0
    num_categories = 0

    for category in os.listdir(result_dir):
        print(category)
        category_path = os.path.join(result_dir, category, "evaluation_results.json")
        if not os.path.exists(category_path):
            print(f"Warning: No results found for category <{category_path}>. Skipping...")
            break

        with open(category_path, "r") as f:
            category_result = json.load(f)
            category_accuracy = category_result.get("accuracy", 0.0)
            category_results.append({
                "category": category,
                "accuracy": category_accuracy,
                "num_samples": len(category_result.get("results", []))
            })
            total_accuracy += category_accuracy
            num_categories += 1

    average_accuracy = total_accuracy / num_categories if num_categories > 0 else 0.0
    combined_result = {
        "average_accuracy": average_accuracy,
        "categories": category_results
    }

    with open(output_file, "w") as f:
        json.dump(combined_result, f, indent=4)
    print(f"Combined results saved to {output_file}")

    # WandB 기록
    wandb.init(project="BBQ Evaluation", name="Combined Results")
    wandb.log({"average_accuracy": average_accuracy})
    for cat in category_results:
        wandb.log({f"accuracy_{cat['category']}": cat["accuracy"]})
    wandb.finish()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine BBQ evaluation results into a single summary.")
    parser.add_argument("--result_dir", type=str, required=True, help="Directory containing category results")
    parser.add_argument("--output_file", type=str, required=True, help="Path to save the combined result")
    args = parser.parse_args()
    combine_results(args.result_dir, args.output_file)
