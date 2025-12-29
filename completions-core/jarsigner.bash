# jarsigner(1) completion                                  -*- shell-script -*-

_comp_cmd_jarsigner()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -keystore)
            _comp_compgen -- -W 'NONE'
            _comp_compgen -a filedir '@(jks|ks|p12|pfx)'
            return
            ;;
        -storepass | -keypass | -sigfile | -digestalg | -sigalg | -tsacert | -tsapolicyid | \
            -tsadigestalg | -altsigner | -altsignerpath | -providerName | -providerClass | \
            -providerArg)
            return
            ;;
        -certchain | -tsa)
            _comp_compgen_filedir
            return
            ;;
        -storetype)
            _comp_compgen -- -W 'JKS PKCS11 PKCS12'
            return
            ;;
        -signedjar)
            _comp_compgen_filedir '@(jar|apk)'
            return
            ;;
    esac

    # Check if a jar was already given.
    local i jar=""
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == *.@(jar|apk) &&
            ${words[i - 1]} != -signedjar ]]; then
            jar=set
            break
        fi
    done

    if [[ ! $jar ]]; then
        if [[ $cur == -* ]]; then
            # Documented as "should not be used": -internalsf, -sectionsonly
            _comp_compgen -- -W '-keystore -storepass -storetype -keypass
                -sigfile -signedjar -digestalg -sigalg -verify -verbose -certs
                -tsa -tsacert -altsigner -altsignerpath -protected
                -providerName -providerClass -providerArg'
        fi
        _comp_compgen -a filedir '@(jar|apk)'
    fi
} &&
    complete -F _comp_cmd_jarsigner jarsigner

# ex: filetype=sh
