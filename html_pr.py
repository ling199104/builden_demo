import os.path

def pr():
    with open('44509.txt','r',encoding='utf-8') as f:
        txt = f.read()
    txt = txt.split(',')
    for i in range(1,len(txt)+1):
        if len(txt[i-1])>20:
            txt[i-1] = ' ' + str(i//5+1) + '. ' + txt[i-1] + '<br>'
        else:
            txt[i-1] = txt[i-1] + '<br>'
    txt = (',').join(txt)
    txt = txt.replace('(','<button type="button" class="btn btn-Default">')
    txt = txt.replace(')','</button>')
    return(txt.replace(',','').replace(';',','))
def oz():
    q1 ="""
{% extends "base.html" %}

{% block title %}Build-En{% endblock %}

{% block page_content %}
<h1><strong>第 壹 部 分 ： 單 選 題</strong></h1>
<!--<div class="tab-content" style="font-size:36px">-->
<div class="tab-content" style="font-size:36px;">
    <!--<div id="home" class="tab-pane fade in active">-->
    <div id="home" class="tab-pane fade in active">
        <h2><strong>一、詞 彙 題</strong></h2><h3 style="line-height:40px">
    """
    q2 ="""
        <br></h3>
    </div>
    <!--<div id="menu1" class="tab-pane fade">-->
    <div id="menu1" class="tab-pane fade in active">
        <h2><strong>二、綜合測驗</strong></h2><h3 style="line-height:40px">Bill and Sam decided to kidnap the son of a banker to compensate for their business loss. They kidnapped the boy and hid him in a cave. They asked for a ransom of $2,000 to return the boy. 16 , their plan quickly got out of control. Their young captive 17 to be a mischievous boy. He viewed the kidnapping as a wonderful camping trip. He demanded that his kidnappers play tiring games with him, such as riding Bill as a horse for nine miles. Bill and Sam were soon desperate and decided to 18 the little terror. They lowered the price to $1,500. Yet, knowing perfectly well 19 a troublemaker his son was, the father refused to give them any money. 20 , he asked the kidnappers to pay him $250 to take the boy back. To persuade the boy to return home, Bill and Sam had to tell him that his father was taking him bear-hunting. The kidnappers finally handed over the boy and $250 to the banker and fled town as quickly as they could.<br>
        16. <br><button type="button" class="btn btn-Default">A</button> However <br><button type="button" class="btn btn-Default">B</button> Otherwise <br><button type="button" class="btn btn-Default">C</button> Furthermore <br><button type="button" class="btn btn-Default">D</button> Accordingly<br>17. <br><button type="button" class="btn btn-Default">A</button> made believe <br><button type="button" class="btn btn-Default">B</button> got along <br><button type="button" class="btn btn-Default">C</button> turned out <br><button type="button" class="btn btn-Default">D</button> felt like<br>18. <br><button type="button" class="btn btn-Default">A</button> hold on to <br><button type="button" class="btn btn-Default">B</button> get rid of <br><button type="button" class="btn btn-Default">C</button> make fun of <br><button type="button" class="btn btn-Default">D</button> take advantage of<br>19. <br><button type="button" class="btn btn-Default">A</button> how <br><button type="button" class="btn btn-Default">B</button> that <br><button type="button" class="btn btn-Default">C</button> why <br><button type="button" class="btn btn-Default">D</button> what<br>20. <br><button type="button" class="btn btn-Default">A</button> Namely <br><button type="button" class="btn btn-Default">B</button> Altogether <br><button type="button" class="btn btn-Default">C</button> Simply <br><button type="button" class="btn btn-Default">D</button> Instead<br></h3>
    </div>
    <div id="menu2" class="tab-pane fade in active">
        <h2><strong>三、文意選填</strong></h2><h3 style="line-height:40px">Are forests always created by nature? A man from rural India proves that this is not necessarily ______. Abdul Kareem, who used to be an airline ticketing agent, has a great love for the woods. Though he never went to college, he can talk about plants and trees like an expert. In 1977, he bought a piece of rocky wasteland with the ______ of growing trees on it. In the beginning, people thought he was ______ to waste his time and money on the land. But he simply ______ them and kept working on the soil and planting trees there. The land was so ______ that it had to be watered several times a day. Kareem had to fetch the water from a source that was a kilometer away. In the first two years, none of the trees he planted ______ . However, in the third year, several young trees started growing. Greatly ______ by the result, Kareem planted more trees and his man-made forest began to take shape. Kareem let his forest grow naturally, without using fertilizers or insecticides. He believed in the ability of nature to renew itself without the ______ of humans. That’s why he did not allow fallen leaves or twigs from the forest to be removed. After years of hard work, Kareem has not only realized his dream but also transformed a piece of ______ property into a beautiful forest. Today, his forest is home to 1,500 medicinal plants, 2,000 varieties of trees, rare birds, animals, and insects. Now, scientists from all over the world come to visit his ______ . They hope to find the secret of his success.<br>
		<button type="button" class="btn btn-Default">A</button> deserted <button type="button" class="btn btn-Default">B</button> interference <button type="button" class="btn btn-Default">C</button> vision <button type="button" class="btn btn-Default">D</button> crazy <button type="button" class="btn btn-Default">E</button> creation <br>
		<button type="button" class="btn btn-Default">F</button> encouraged <button type="button" class="btn btn-Default">G</button> ignored <button type="button" class="btn btn-Default">H</button> survived <button type="button" class="btn btn-Default">I</button> dry <button type="button" class="btn btn-Default">J</button> true<br></h3>
    </div>
    <div id="menu3" class="tab-pane fade in active">
        <h2><strong>四、閱讀測驗</strong></h2><h3 style="line-height: 40px">Type-A people are generally considered sensitive perfectionists and good team players, but over-anxious. Type Os are curious and generous but stubborn. Type ABs are artistic but mysterious and unpredictable, and type Bs are cheerful but eccentric, individualistic, and selfish. Though lacking scientific evidence, this belief is widely seen in books, magazines, and television shows. The blood-type belief has been used in unusual ways. The women’s softball team that won gold for Japan at the Beijing Olympics is reported to have used blood-type theories to customize training for each player. Some kindergartens have adopted teaching methods along blood group lines, and even major companies reportedly make decisions about assignments based on an employee’s blood type. In 1990, Mitsubishi Electronics was reported to have announced the formation of a team composed entirely of AB workers, thanks to “their ability to make plans.” The belief even affects politics. One former prime minister considered it important enough to reveal in his official profile that he was a type A, while his opposition rival was type B. In 2011, a minister, Ryu Matsumoto, was forced to resign after only a week in office, when a bad-tempered encounter with local officials was televised. In his resignation speech, he blamed his failings on the fact that he was blood type B. The blood-type craze, considered simply harmless fun by some Japanese, may manifest itself as prejudice and discrimination. In fact, this seems so common that the Japanese now have a term for it: burahara, meaning blood-type harassment. There are reports of discrimination leading to children being bullied, ending of happy relationships, and loss of job opportunities due to blood type.</h3>
    </div>
</div>
<!--h1><strong>第 貳 部 分 ： 非 選 擇 題</strong></h1-->
{% endblock %}
    """
    quiz = q1 + pr() + q2
    return quiz

completeName = os.path.join(r'F:\Python3.5.2_x64\PythonProjects\template_demo\templates\\', "quiz.html")
with open(completeName,'w',encoding='utf-8') as f:
    f.write(oz())
if __name__=="__main__":
    print(pr())
