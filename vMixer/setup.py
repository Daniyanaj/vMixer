from setuptools import setup, find_namespace_packages

setup(name='vmixer',
      packages=find_namespace_packages(include=["vmixer", "vmixer.*"]),
      install_requires=[
            "torch>=1.6.0a",
            "tqdm",
            "dicom2nifti",
            "scikit-image>=0.14",
            "medpy",
            "scipy",
            "batchgenerators>=0.21",
            "numpy",
            "sklearn",
            "SimpleITK",
            "pandas",
            "requests",
            "nibabel", 'tifffile'
      ],
      entry_points={
          'console_scripts': [
              'vmixer_convert_decathlon_task = vmixer.experiment_planning.vmixer_convert_decathlon_task:main',
              'vmixer_plan_and_preprocess = vmixer.experiment_planning.vmixer_plan_and_preprocess:main',
              'vmixer_train = vmixer.run.run_training:main',
              'vmixer_train_DP = vmixer.run.run_training_DP:main',
              'vmixer_train_DDP = vmixer.run.run_training_DDP:main',
              'vmixer_predict = vmixer.inference.predict_simple:main',
              'vmixer_ensemble = vmixer.inference.ensemble_predictions:main',
              'vmixer_find_best_configuration = vmixer.evaluation.model_selection.figure_out_what_to_submit:main',
              'vmixer_print_available_pretrained_models = vmixer.inference.pretrained_models.download_pretrained_model:print_available_pretrained_models',
              'vmixer_print_pretrained_model_info = vmixer.inference.pretrained_models.download_pretrained_model:print_pretrained_model_requirements',
              'vmixer_download_pretrained_model = vmixer.inference.pretrained_models.download_pretrained_model:download_by_name',
              'vmixer_download_pretrained_model_by_url = vmixer.inference.pretrained_models.download_pretrained_model:download_by_url',
              'vmixer_determine_postprocessing = vmixer.postprocessing.consolidate_postprocessing_simple:main',
              'vmixer_export_model_to_zip = vmixer.inference.pretrained_models.collect_pretrained_models:export_entry_point',
              'vmixer_install_pretrained_model_from_zip = vmixer.inference.pretrained_models.download_pretrained_model:install_from_zip_entry_point',
              'vmixer_change_trainer_class = vmixer.inference.change_trainer:main',
              'vmixer_evaluate_folder = vmixer.evaluation.evaluator:vmixer_evaluate_folder',
              'vmixer_plot_task_pngs = vmixer.utilities.overlay_plots:entry_point_generate_overlay',
          ],
      },
      
      )
