EXP_FOL=/home/nlpgpu7/ellt/suyun/bbq_accuracy/EXP_FOL_bert

python /home/nlpgpu7/ellt/suyun/bbq_accuracy/evaluation/combine_results.py \
    --result_dir ${EXP_FOL}/bbq \
    --output_file ${EXP_FOL}/bbq/combined_results.json