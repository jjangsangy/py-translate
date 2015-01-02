#!/usr/bin/env bash
# ==============================================================================
usage () { cat <<- DOCUMENT

    AUTHOR:      Sang Han

    Benchmark py-translation

    USAGE:

        ./language_bench.sh [-h]

    OPTIONAL ARGUMENTS:

        [-h]: Prints out this help message and exit

	DOCUMENT

    return 0
}


# ===============================================================================
# Language Codes
# ===============================================================================

declare -a codes=(
    'af' 'ar' 'az' 'be' 'bg' 'bn' 'bs' 'ca' 'ceb'
    'cs' 'cy' 'da' 'de' 'el' 'en' 'eo' 'es' 'et'
    'eu' 'fa' 'fi' 'fr' 'ga' 'gl' 'gu' 'hi' 'hmn'
    'hr' 'ht' 'hu' 'id' 'is' 'it' 'iw' 'ja' 'jw'
    'ka' 'km' 'kn' 'ko' 'la' 'lo' 'lt' 'lv' 'mk'
    'mr' 'ms' 'mt' 'nl' 'no' 'pl' 'pt' 'ro' 'ru'
    'sk' 'sl' 'sq' 'sr' 'sv' 'sw' 'ta' 'te' 'th'
    'tl' 'tr' 'uk' 'ur' 'vi' 'yi' 'zh' 'zh-TW'
)

# ===============================================================================
# Option Parser
# ===============================================================================
while getopts ":h" OPTION; do
    case ${OPTION} in
        h) usage
           exit 0
           ;;
    esac
done
    shift $((OPTIND-1))


# ===============================================================================
# Main
# ===============================================================================
function main()
{
    local input="../texts/alice.txt"
    local output="raw.txt"
    local source="en"

    for target in "${codes[@]}"; do
    {
        printf "%s" "${target}" >> "${output}"
        {
            time translate "${source}" "${target}" < "${input}"
        } 2> >(grep 'real' | sed 's/real//' | tee -a "${output}")

    }

    done
}

# ===============================================================================
# Entry Point
# ===============================================================================
if [ "${0}" = "${BASH_SOURCE}" ]; then
    main "$@"
fi
