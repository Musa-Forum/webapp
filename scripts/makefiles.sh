#!/bin/sh

usage="Usage: $0 num"
if [ $# -ne 1 ]; then
    echo $usage
    exit -1
fi

num=$1


quiz=$(python3 getquiz.py $num)
echo $quiz
setopt shwordsplit
IFS=,
set -- $quiz
quizquiz=$1
choice1=$2
choice2=$3
choice3=$4
answer=$5
japanese_name=$6
english_name=$7

cd ../templates

mkdir $english_name
cd $english_name
touch $english_name.html
touch ${english_name}_correct.html
touch ${english_name}_incorrect.html


### quiz.html ###
echo '{% extends "layout_quiz.html" %}' >> $english_name.html
echo "\n" >> $english_name.html
echo "{% block title %}" >> $english_name.html
echo "${japanese_name}クイズ" >> $english_name.html
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block quiz %}" >> $english_name.html
echo "$quizquiz" >> $english_name.html
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block picture %}" >> $english_name.html
echo '"/static/images/'"${english_name}"'_silhouette.png"' >> $english_name.html
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block answer1 %}" >> $english_name.html
if [ $answer -eq 1 ]; then
    echo '"location.href='\''./'"${english_name}"'_correct'\''"' >> $english_name.html
else
    echo '"location.href='\''./'"${english_name}"'_incorrect'\''"' >> $english_name.html
fi
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block choice1 %}" >> $english_name.html
echo "$choice1" >> $english_name.html
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block answer2 %}" >> $english_name.html
if [ $answer -eq 2 ]; then
    echo '"location.href='\''./'"${english_name}"'_correct'\''"' >> $english_name.html
else
    echo '"location.href='\''./'"${english_name}"'_incorrect'\''"' >> $english_name.html
fi
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block choice2 %}" >> $english_name.html
echo "$choice2" >> $english_name.html
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block answer3 %}" >> $english_name.html
if [ $answer -eq 3 ]; then
    echo '"location.href='\''./'"${english_name}"'_correct'\''"' >> $english_name.html
else
    echo '"location.href='\''./'"${english_name}"'_incorrect'\''"' >> $english_name.html
fi
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

echo "{% block choice3 %}" >> $english_name.html
echo "$choice3" >> $english_name.html
echo "{% endblock %}" >> $english_name.html
echo "\n" >> $english_name.html

### quiz_correct.html ###
echo '{% extends "layout_correct.html" %}' >> ${english_name}_correct.html
echo "\n" >> ${english_name}_correct.html
echo "{% block title %}" >> ${english_name}_correct.html
echo "${japanese_name}クイズ" >> ${english_name}_correct.html
echo "{% endblock %}" >> ${english_name}_correct.html
echo "\n" >> ${english_name}_correct.html
echo "{% block interpretation %}" >> ${english_name}_correct.html
echo "解説" >> ${english_name}_correct.html
echo "{% endblock %}" >> ${english_name}_correct.html
echo "\n" >> ${english_name}_correct.html
echo "{% block picture %}" >> ${english_name}_correct.html
echo '"/static/images/'"${english_name}"'.png"' >> ${english_name}_correct.html
echo "{% endblock %}" >> ${english_name}_correct.html

### quiz_incorrect.html ###
echo '{% extends "layout_incorrect.html" %}' >> ${english_name}_incorrect.html
echo "\n" >> ${english_name}_incorrect.html
echo "{% block title %}" >> ${english_name}_incorrect.html
echo "${japanese_name}クイズ" >> ${english_name}_incorrect.html
echo "{% endblock %}" >> ${english_name}_incorrect.html
echo "\n" >> ${english_name}_incorrect.html
echo "{% block quizpage %}" >> ${english_name}_incorrect.html
echo '"location.href='\''./'"$english_name"\''"' >> ${english_name}_incorrect.html
echo "{% endblock %}" >> ${english_name}_incorrect.html

echo "************ app.pyへ貼り付け ****************" 
echo "#$english_name"
echo '@app.route("/'"$english_name"'",methods=["GET"])'
echo "def ${english_name}():"
echo "\t""return render_template("\'"/${english_name}/${english_name}.html"\'")\n"

echo '@app.route("/'"$english_name"'_correct",methods=["GET"])'
echo "def ${english_name}_correct():"
echo "\t""return render_template("\'"/${english_name}/${english_name}_correct.html"\'")\n"

echo '@app.route("/'"$english_name"'_incorrect",methods=["GET"])'
echo "def ${english_name}_incorrect():"
echo "\t""return render_template("\'"/${english_name}/${english_name}_incorrect.html"\'")\n"

echo "*********** quiztop.htmlへ貼り付け ***************"
echo '<button type="button" class="btn btn-primary" onclick="location.href='\'"$english_name"\''"'">$japanese_name</button>"
