import os

naomi_step256_mimic_ppg_test = {'modelname':'naomi', "annotate":"_step256_mimic_ppg", 'modeltype':'naomi', 
            "annotate_test":"_test",
            "data_name":"mimic_ppg","data_load": {"mean":True, "bounds":1, "train":False, "val":False, "test":True, "addmissing":True},
            "modelparams":{"params":{   'batch' : 2,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'dec128_dim' : 200,
                                        'dec256_dim' : 200,
                                        'dec512_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 256,
                                        'stochastic': False
                                    }, 
                "pretrain_iters":50, "val_iters":10,
                "clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 20, "max_iter_num":60000,
                "save_model_interval":100, "log_interval":10,
                "reload_epoch":3600},
            "train":{"gpus":[0]}}
naomi_britsgail_mimic_ppg_test = {'modelname':'naomi', "annotate":"_britsgail_mimic_ppg", 'modeltype':'naomi', 
            "annotate_test":"_test",
            "data_name":"mimic_ppg","data_load": {"mean":True, "bounds":1, "train":False, "val":False, "test":True, "addmissing":True},
            "modelparams":{"params":{   'batch' : 2,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_iters":50, "val_iters":10,
                "clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 20, "max_iter_num":60000,
                "save_model_interval":100, "log_interval":10,
                "reload_epoch":2200},
            "train":{"gpus":[0]}}



naomi_britsgail_mimic_ecg_test = {'modelname':'naomi', "annotate":"_britsgail_mimic_ecg", 'modeltype':'naomi', 
            "annotate_test":"_test",
            "data_name":"mimic_ecg","data_load": {"train":False, "val":False, "test":True, "addmissing":True},
            "modelparams":{"params":{   'batch' : 2,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_iters":50, "val_iters":10,
                "clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 20, "max_iter_num":60000,
                "save_model_interval":100, "log_interval":10,
                "reload_epoch":200},
            "train":{"gpus":[0]}}

naomi_step256_mimic_ecg_test= {'modelname':'naomi', "annotate":"_step256_mimic_ecg", 'modeltype':'naomi', 
            "annotate_test":"_test",
            "data_name":"mimic_ecg","data_load": {"train":False, "val":False, "test":True, "addmissing":True},
            "modelparams":{"params":{   'batch' : 4,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'dec128_dim' : 200,
                                        'dec256_dim' : 200,
                                        'dec512_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 256,
                                        'stochastic': False
                                    }, 
                "val_iters":10,"pretrain_iters":0,
                "reload_epoch":"pretrain",
                "pretrain_epochs":0,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 0, "max_iter_num":60000,
                "save_model_interval":100, "log_interval":10,
                "reload_epoch":200},
            "train":{"gpus":[0]}}

            


naomi_step256_extended_ptbxl_testextended_10percent = {'modelname':'naomi', "annotate":"_step256_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_10percent",
            "data_name":"ptbxl",
            "data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":100},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'dec128_dim' : 200,
                                        'dec256_dim' : 200,
                                        'dec512_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 256,
                                        'stochastic': False
                                    }, 
                "reload_epoch":3000,
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100},
            "train":{"gpus":[0]}}
naomi_step256_extended_ptbxl_testextended_20percent = {'modelname':'naomi', "annotate":"_step256_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_20percent",
            "data_name":"ptbxl",
            "data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":200},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'dec128_dim' : 200,
                                        'dec256_dim' : 200,
                                        'dec512_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 256,
                                        'stochastic': False
                                    }, 
                "reload_epoch":3000,
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100},
            "train":{"gpus":[0]}}
naomi_step256_extended_ptbxl_testextended_30percent = {'modelname':'naomi', "annotate":"_step256_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_30percent",
            "data_name":"ptbxl",
            "data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":300},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'dec128_dim' : 200,
                                        'dec256_dim' : 200,
                                        'dec512_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 256,
                                        'stochastic': False
                                    }, 
                "reload_epoch":3000,
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100},
            "train":{"gpus":[0]}}
naomi_step256_extended_ptbxl_testextended_40percent = {'modelname':'naomi', "annotate":"_step256_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_40percent",
            "data_name":"ptbxl",
            "data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":400},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'dec128_dim' : 200,
                                        'dec256_dim' : 200,
                                        'dec512_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 256,
                                        'stochastic': False
                                    }, 
                "reload_epoch":3000,
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100},
            "train":{"gpus":[0]}}
naomi_step256_extended_ptbxl_testextended_50percent = {'modelname':'naomi', "annotate":"_step256_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_50percent",
            "data_name":"ptbxl",
            "data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":500},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'dec128_dim' : 200,
                                        'dec256_dim' : 200,
                                        'dec512_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 256,
                                        'stochastic': False
                                    }, 
                "reload_epoch":3000,
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100},
            "train":{"gpus":[0]}}


            
naomi_britsgail_extended_ptbxl_testextended_10percent = {'modelname':'naomi', "annotate":"_britsgail_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_10percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":100},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":6500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_extended_ptbxl_testextended_20percent = {'modelname':'naomi', "annotate":"_britsgail_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_20percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":200},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":6500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_extended_ptbxl_testextended_30percent = {'modelname':'naomi', "annotate":"_britsgail_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_30percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":300},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":6500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_extended_ptbxl_testextended_40percent = {'modelname':'naomi', "annotate":"_britsgail_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_40percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":400},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":6500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_extended_ptbxl_testextended_50percent = {'modelname':'naomi', "annotate":"_britsgail_extended_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testextended_50percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_extended":500},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":6500
                },
            "train":{"gpus":[0]}}




naomi_britsgail_transient_ptbxl_testtransient_10percent = {'modelname':'naomi', "annotate":"_britsgail_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_10percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.10}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":15500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_transient_ptbxl_testtransient_20percent = {'modelname':'naomi', "annotate":"_britsgail_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_20percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.20}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":15500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_transient_ptbxl_testtransient_30percent = {'modelname':'naomi', "annotate":"_britsgail_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_30percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.30}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":15500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_transient_ptbxl_testtransient_40percent = {'modelname':'naomi', "annotate":"_britsgail_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_40percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.40}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":15500
                },
            "train":{"gpus":[0]}}
naomi_britsgail_transient_ptbxl_testtransient_50percent = {'modelname':'naomi', "annotate":"_britsgail_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_50percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.50}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 1,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":15500
                },
            "train":{"gpus":[0]}}



naomi_step64_transient_ptbxl_testtransient_10percent = {'modelname':'naomi', "annotate":"_step64_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_10percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.10}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 64,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":14500
                },
            "train":{"gpus":[0]}}

naomi_step64_transient_ptbxl_testtransient_20percent = {'modelname':'naomi', "annotate":"_step64_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_20percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.20}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 64,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":14500
                },
            "train":{"gpus":[0]}}

naomi_step64_transient_ptbxl_testtransient_30percent = {'modelname':'naomi', "annotate":"_step64_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_30percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.30}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 64,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":14500
                },
            "train":{"gpus":[0]}}

naomi_step64_transient_ptbxl_testtransient_40percent = {'modelname':'naomi', "annotate":"_step64_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_40percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.40}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 64,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":14500
                },
            "train":{"gpus":[0]}}

naomi_step64_transient_ptbxl_testtransient_50percent = {'modelname':'naomi', "annotate":"_step64_transient_ptbxl", 'modeltype':'naomi', 
            "annotate_test":"_testtransient_50percent",
            "data_name":"ptbxl","data_load": {"mode":True, "bounds":1, "channels":[0], "impute_transient":{"window":5, "prob":.50}},
            "modelparams":{"params":{   'batch' : 1,
                                        'y_dim' : 1,
                                        'rnn_dim' : 300,
                                        'dec1_dim' : 200,
                                        'dec2_dim' : 200,
                                        'dec4_dim' : 200,
                                        'dec8_dim' : 200,
                                        'dec16_dim' : 200,
                                        'dec32_dim' : 200,
                                        'dec64_dim' : 200,
                                        'n_layers' : 2,
                                        'discrim_rnn_dim' : 128,
                                        'discrim_num_layers' : 1,
                                        'cuda' : True,
                                        'highest' : 64,
                                        'stochastic': False
                                    }, 
                "pretrain_epochs":20,"clip" :10,
                "policy_learning_rate":1e-6, "discrim_learning_rate":1e-3,"pre_start_lr":1e-3,
                "pretrain_disc_iter" : 2000, "max_iter_num":60000,
                "save_model_interval":500, "log_interval":100,
                "reload_epoch":14500
                },
            "train":{"gpus":[0]}}
