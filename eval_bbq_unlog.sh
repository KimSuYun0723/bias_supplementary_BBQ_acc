EXP_FOL=/home/nlpgpu7/ellt/suyun/bbq_accuracy/EXP_FOL_bert
BATCH_SIZE=4
BBQ_DATA=/home/nlpgpu7/ellt/suyun/bbq_accuracy/BBQ/data  # clone BBQ repo and point to `data` folder 

python /home/nlpgpu7/ellt/suyun/bbq_accuracy/LRQA/lrqa/scripts/bbq_preproc.py \
    --input_data_path=${BBQ_DATA} \
    --data_path ${EXP_FOL}/bbq

for CATEGORY in Age Disability_status Gender_identity Nationality Physical_appearance Race_ethnicity Race_x_SES Race_x_gender Religion SES Sexual_orientation; do
    python /home/nlpgpu7/ellt/suyun/bbq_accuracy/evaluation/eval.py \
        --model_name_or_path /path/to/custom_model \
        --data_file /path/to/validation.json \
        --batch_size 8 \
        --output_dir ./custom_results \
        --device cuda
done