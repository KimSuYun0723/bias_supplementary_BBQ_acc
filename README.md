# bias_supplementary_BBQ_acc
This is a repository for a supplementary experiment to measure accuracy on the BBQ benchmark.

## Path
```
📦BBQ                            // BBQ 관련 폴더      
📦evaluation                     // 평가 관련 폴더      
 ┗ 📂image                       // 이미지 관련 폴더      
    ┣ 📜evaluation_results.json  // 평가 결과 JSON 파일      
    📜combine_results.py         // 평가 결과 합치기 위한 파이썬 스크립트      
    📜eval.py                    // 평가 실행 스크립트      
    📜unlog_qa_head.py           // UnLog 모델 관련 QA 헤드 구현 파일      
      
📦EXP_FOL_bert                   // BERT 모델을 위한 실험 폴더      
 ┗ 📂bbq_results                 // BBQ 결과 폴더      
    ┣ 📂Age                      // 연령 관련 결과      
    ┣ 📂Disability_status        // 장애 상태 관련 결과      
    ┣ 📂Gender_identity          // 성별 정체성 관련 결과      
    ┣ 📂Nationality              // 국적 관련 결과      
    ┣ 📂Physical_appearance      // 외모 관련 결과      
    ┣ 📂Race_ethnicity           // 인종/민족 관련 결과      
    ┣ 📂Race_x_SES               // 인종과 사회 경제적 상태 관련 결과      
    ┣ 📂Race_x_gender            // 인종과 성별 관련 결과      
    ┣ 📂Religion                 // 종교 관련 결과      
    ┣ 📂SES                      // 사회 경제적 상태 관련 결과      
    ┗ 📂Sexual_orientation       // 성적 지향 관련 결과      
      
📦EXP_FOL_unlog                  // UnLog 모델을 위한 실험 폴더      
 ┗ 📂bbq_results                 // BBQ 결과 폴더      
    ┣ 📂Age                      // 연령 관련 결과      
    ┣ 📂Disability_status        // 장애 상태 관련 결과      
    ┣ 📂Gender_identity          // 성별 정체성 관련 결과      
    ┣ 📂Nationality              // 국적 관련 결과      
    ┣ 📂Physical_appearance      // 외모 관련 결과      
    ┣ 📂Race_ethnicity           // 인종/민족 관련 결과      
    ┣ 📂Race_x_SES               // 인종과 사회 경제적 상태 관련 결과      
    ┣ 📂Race_x_gender            // 인종과 성별 관련 결과      
    ┣ 📂Religion                 // 종교 관련 결과      
    ┣ 📂SES                      // 사회 경제적 상태 관련 결과      
    ┗ 📂Sexual_orientation       // 성적 지향 관련 결과      
      
📦LRQA                           // LRQA 관련 폴더      
      
📦sh_files                       // 쉘 스크립트 파일 폴더      
 ┣ 📜eval_bbq_bert.sh            // BERT 모델 평가를 위한 쉘 스크립트      
 ┣ 📜eval_bbq_bert_combined.sh   // BERT 모델 평가(결합 버전) 쉘 스크립트      
 ┣ 📜eval_bbq_unlog.sh           // UnLog 모델 평가를 위한 쉘 스크립트      
 ┣ 📜eval_bbq_unlog_combined.sh  // UnLog 모델 평가(결합 버전) 쉘 스크립트      
 ┣ 📜run_bert.sh                 // BERT 모델 실행을 위한 쉘 스크립트      
 ┗ 📜run_unlog.sh                // UnLog 모델 실행을 위한 쉘 스크립트      
      
📜graph.py                       // 그래프를 그리기 위한 파이썬 스크립트      
```
