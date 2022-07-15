from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def えへっ (ctx):
    await ctx.send('「えへっ」てなんだよ‼')

@bot.command()
setlist =['大地を流浪する楽団','剣闘士のフィナーレ','雷を鎮める尊者','烈火を渡る尊者','愛される少女','翠緑の影','雷のような怒り','燃え盛る炎の魔女','旧貴族のしつけ','血染めの騎士道','悠久の盤岩','逆飛びの流星','絶縁の旗印','追憶のしめ縄','沈淪の心','氷風を彷徨う勇士','千岩牢固','蒼白の炎','海染硨磲','華館夢醒形骸記']
mainlist ={'防御力':'58.3%','攻撃力':'46.6%','HP':'46.6%','元素熟知 ':'187'}
mainlist0 ={'HP ':'4780'}
mainlist1 ={'攻撃力 ':'311'}
mainlist2 ={'元素チャージ効率':'51.8%'}
mainlist3 ={'炎ダメージ':'46.6%','氷ダメージ':'46.6%','水ダメージ':'46.6%','雷ダメージ':'46.6%','風ダメージ':'46.6%','岩ダメージ':'46.6%','物理ダメージ':'58.3%'}
mainlist4 ={'与える治癒効果':'35.9%','会心ダメージ':'62.2%','会心率':'31.1%'}
mainstalist ={'花':mainlist0,'羽':mainlist1,'時計':mainlist2 ,'杯':mainlist3,'冠':mainlist4}
#サブステータスリスト
numberlist ={'HP ':0,'HP':1,'攻撃力 ':2,'攻撃力':3,'会心率':4,'会心ダメージ':5,'防御力':7,'元素チャージ効率':8,'元素熟知 ':9}
sublist =['HP ','HP','攻撃力 ','攻撃力','会心率','会心ダメージ','防御力 ','防御力','元素チャージ効率','元素熟知 ']
ssuu ={'HP ':[209,239,269,299],'HP':[4.1,4.7,5.3,5.8],'攻撃力 ':[14,16,18,19],'攻撃力':[4.1,4.7,5.3,5.8],'会心率':[2.7,3.1,3.5,3.9],'会心ダメージ':[5.4,6.2,7.0,7.8],'防御力 ':[16,19,21,23],'防御力':[5.1,5.8,6.6,7.3],'元素チャージ効率':[4.5,5.2,5.8,6.5],'元素熟知 ':[16,19,21,23]}
#厳選関数の設定       
def gensen(mainsta,number,sublist):  
    #サブステータスリストからメインステータスを削除
    x = random.randint(1,2)
    sublist.pop(number)
    #メインステータスがダメージバフか治癒効果の時に消してしまった元素熟知を追加
    if 'ダメージ' in mainsta:
        sublist.append('元素熟知')
    elif '治癒効果' in mainsta:
        sublist.append('元素熟知')
    s =random.randint(0,8)
    sub1 = sublist.pop(s)
    a =random.randint(1,1+x+3)
    result1 = 0
    for i in range(a):
        xx =random.randint(0,3)
        ss = ssuu[sub1][xx]
        result1= result1 + ss
    score = 0
    if sub1 =='会心率':
        score = score+result1*2
    elif sub1 =='会心ダメージ':
        score = score + result1
    elif sub1 == '攻撃力':
        score = score +result1
    if ' 'in sub1:
        result1 =result1
    else:
        result1 =str(result1)+'％'
    s =random.randint(0,7)
    sub2 = sublist.pop(s)
    b = random.randint(1,x+4-a+1)
    result2 =0
    for count in range(b):
        xx =random.randint(0,3)
        ss = ssuu[sub2][xx]
        result2 = result2 +ss
    if sub2 =='会心率':
        score = score+result2*2
    elif sub2 =='会心ダメージ':
        score = score +result2
    elif sub2 == '攻撃力':

        score = score +result2
    if ' 'in sub2:
        result2 =result2
    else:
        result2 =str(result2)+'％'
    s =random.randint(0,6)
    sub3 = sublist.pop(s)
    c = random.randint(1,x+4-a+1-b+1)
    result3 =0
    for count in range(c):
        xx = random.randint(0,3)
        ss = ssuu[sub3][xx]
        result3 =result3 +ss
    if sub3 =='会心率':
        score = score+result3*2
    elif sub3 =='会心ダメージ':
        score = score + result3
    elif sub3 == '攻撃力':
        score = score +result3
    if ' 'in sub3:
        result3 =result3
    else:
        result3 =str(result3)+'％'
    s =random.randint(0,5)
    sub4 = sublist.pop(s)
    d = random.randint(1,x+4-a+1-b+1-c+1)
    result4 =0
    for count in range(d):
        xx =random.randint(0,3)
        ss=ssuu[sub4][xx]
        result4 =result4 +ss
    if sub4 =='会心率':
        score = score+result4*2
    elif sub4 =='会心ダメージ':
        score = score + result4
    elif sub4 == '攻撃力':
        score = score +result4
    if ' 'in sub4:
        result4 = result4
    else:
        result4 = str(result4)+'％'
    return sub1,result1,sub2,result2,sub3,result3,sub4,result4,score
def gense(sublist,mainlist):
    sublist =sublist
    main = random.randint(0,4)
    mainn = list(mainstalist.keys())[main]
    List = list(mainstalist.values())[main]
    if List == mainlist0:
        mainlist =mainlist0
    elif List ==mainlist1:
        mainlist = mainlist1
    else:
        mainlist.update(List)
    a =len(mainlist)
    x = random.randint(0,a-1)
    mainsta = list(mainlist.keys())[x]
    mainnum =list(mainlist.values())[x]
    if 'ダメージ'in mainsta:
        number =9
    elif '治癒効果'in mainsta:
        number=9
    else:
        number = numberlist[mainsta]    
    q,w,e,r,t,y,u,i,score = gensen(mainsta,number,sublist)
    return mainn,mainsta,mainnum,q,w,e,r,t,y,u,i,score
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'gensen':
        mainlist ={'防御力':'58.3%','攻撃力':'46.6%','HP':'46.6%','元素熟知 ':'187'}
        sublist =['HP ','HP','攻撃力 ','攻撃力','会心率','会心ダメージ','防御力 ','防御力','元素チャージ効率','元素熟知 ']
        a = len(setlist) -1
        seiibutunumber= random.randint(0,a)
        seiibutu = setlist[seiibutunumber]
        z,x,c,v,b,n,m,s,d,f,g,h = gense(sublist,mainlist)
        await message.channel.send('```' + str (seiibutu) +'\n' +str(z)+'\n'+str(x) +' '+ str(c) +'\n'+str(v) + ' '+str(b)+'　\n'+str(n) + ' '+str(m)+'　\n'+str(s)+ ' '+str(d)+'　\n'+str(f)+ ' ' + str(g)+'　\n'+'スコア:'+str(h)+'```')
        if h >=20:
            if h >=30:
                if h>=40:
                    if h>=50:
                        comment = ('これはすごい聖遺物だぞ！')
                    else:
                        comment = ('お！なかなかいいぞ！')
                else:
                    comment = ('うーん、なかなかだな！')
            else:
                comment = ('あ...いい感じだな！')
        else:
            comment = ('そういう日もあるよな！')
        await message.channel.send(comment)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
