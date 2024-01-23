# Convert rife models to ncnn online
- Steps to convert:
- Fork repo, and replace train_log with desired model, -- note - have tested with 4.14, but should work with later versions unless an arch change.
- edit config, at the top is the ensemble option. by default it should be false,-
  * fp16 just means 16 bit limit, if disabled it will export 32 bit, usually doesnt make difference.
  * conversion_method, pnnx is only option due to it is the only way to convert on newer distros/python versions.
- Run CI in github actions.
- Download model from output (flownet.bin/flownet.param).


# run locally
- python3 convertscript.py - note, may need to modify pip with --break-system-packages for some distros.
