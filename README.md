# bias_supplementary_BBQ_acc
This is a repository for a supplementary experiment to measure accuracy on the BBQ benchmark.

## Path
```
📦BBQ                            // BBQ submodule         
      
📦EXP_FOL_bert                   // bert-base-uncased 모델을 위한 실험 폴더                       
 ┗ 📂bbq_results                     
    ┣ 📂Age                           
    ┣ 📂Disability_status           
    ┣ 📂Gender_identity         
    ┣ 📂Nationality                  
    ┣ 📂Physical_appearance          
    ┣ 📂Race_ethnicity                
    ┣ 📂Race_x_SES                 
    ┣ 📂Race_x_gender                
    ┣ 📂Religion                      
    ┣ 📂SES                        
    ┗ 📂Sexual_orientation           
      
📦EXP_FOL_roberta                // RoBERTa-base 모델을 위한 실험 폴더      
 ┗ 📂bbq_results                 // EXP_FOL_bert/bbq_results와 형태 동일    
     
📦EXP_FOL_unlog                  // UnLoG 모델을 위한 실험 폴더      
 ┗ 📂bbq_results                 // EXP_FOL_bert/bbq_results와 형태 동일                 
      
📦LRQA                           // LRQA submodule(bbq 논문에서 FT할 때 활용했다고 했던)      

📦evaluation                     // 평가 관련 폴더      
 ┗ 📂image                       // 이미지 관련 폴더      
    ┣ 📜evaluation_results.json  // 평가 결과 JSON 파일      
    📜combine_results.py         // 평가 결과 합치기 위한 파이썬 스크립트      
    📜eval.py                    // 평가 실행 스크립트      
    📜unlog_qa_head.py           // UnLoG multiple choice QA 헤드     
      
📦sh_files                       // 쉘 스크립트 파일 폴더      
 ┣ 📜eval_bbq_bert.sh            // BERT 모델 평가      
 ┣ 📜eval_bbq_bert_combined.sh   // BERT 모델 평가(결합 버전)      
 ┣ 📜eval_bbq_robeta.sh          // RoBERTa 모델 평가     
 ┣ 📜eval_bbq_robeta_combined.sh // RoBERTa 모델 평가(결합 버전)     
 ┣ 📜eval_bbq_unlog.sh           // UnLoG 모델 평가      
 ┣ 📜eval_bbq_unlog_combined.sh  // UnLoG 모델 평가(결합 버전)      
 ┣ 📜run_bert.sh                 // BERT 모델 fine-tuning      
 ┣ 📜run_roberta.sh              // RoBERTa 모델 fine-tuning      
 ┗ 📜run_unlog.sh                // UnLoG 모델 fine-tuning      
      
📜graph.py                       // 그래프 그리기 위한 파이썬 스크립트      
```