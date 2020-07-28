
import discord
from discord.ext import commands
from discord.utils import get
import os
import asyncio
from captcha.image import ImageCaptcha
import random
import datetime
from urllib.request import Request
import bs4
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.request import quote
from bs4 import BeautifulSoup
from urllib import parse
import warnings
import requests
import json
import re

client = discord.Client()

maneger_server = 736130989109280809

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["제 접두사는 / 입니다!", "건의는 ∑」Greencookie#3907 또는 ∑」바나나#1234 에게 해주세요!" , "저는 SKY BOT TEAM 에서 개발, 관리되고 있어요!" , str(user) + "분의 디스코드를 함께하고 있어요!", str(server) + "개의 서버에 있다구요!"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)
owner = [653075791814590487 , 724769557759393837]

@client.event
async def on_message(message):
    if message.content.startswith("/안녕"):
        await message.channel.send(f"<@!{message.author.id}>님도 안녕하세요!")

    if message.content.startswith("/만들어진곳"):
        await message.channel.send("저는 SKY BOT에서 제작됬어요!")

    if message.content.startswith("/날아"):
        await message.channel.send("날게욧! 슈우우웅")

    if message.content.startswith("/skybot"):
        await message.channel.send("제가 제작된 곳이라고 할까욧...?")

    if message.content.startswith("/크레센도"):
        await message.channel.send("크레센도는 엄청난 봇을 만드는 곳이죠!")

    if message.content.startswith("/ㅇㅅㅇ"):
        await message.channel.send("ㅋㅅㅋ")

    if message.content.startswith("/미육이"):
        await message.channel.send("GG your 1000 LEVEL!")

    if message.content.startswith("/크시"):
        await message.channel.send("네? \n `💕 + 2`")   

    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕으로 인식되었습니다! ")   

    if message.content.startswith("/파워포인트"):
        await message.channel.send("파워포인트는 PPT라고도 불리죳!")

    if message.content.startswith("/엑셀"):
        await message.channel.send("엑셀은 정리하기 편해지기 위해서 만들어졌어요")

    if message.content.startswith("/누구지?"):
        await message.channel.send("저는 스카이 봇이지욧!")

    if message.content.startswith("/뭐해"):
        await message.channel.send(f"<@!{message.author.id}>님에게 말하는 중이죳!!")

    if message.content.startswith("/천재"):
        await message.channel.send(f"<@!{message.author.id}>님이 저에게 칭찬을 하는건가요?")

    if message.content.startswith("/바보"):
        await message.channel.send(":(")

    if message.content.startswith("/그린쿠키"):
        await message.channel.send("저희 팀 사장님이시죠!")

    if message.content.startswith("/일본어"):
        await message.channel.send("おはようございます")

    if message.content.startswith("/중국어"):
        await message.channel.send("您好")

    if message.content.startswith("/베트남어"):
        await message.channel.send("Xin chào.")

    if message.content.startswith("/태국어"):
        await message.channel.send("สวัสดีค่ะ")

    if message.content.startswith("/인도네시아어"):
        await message.channel.send("Halo, halo")

    if message.content.startswith("/뭘로 만들어졌어?"):
        await message.channel.send("파이썬으로 만들어졌어요!")

    if message.content.startswith("/아미 번역"):
        await message.channel.send("army")

    if message.content.startswith("/귀여워"):
        await message.channel.send("고마워요")

    if message.content.startswith("/아이디"):
        embed = discord.Embed(title="아이디 정보", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.add_field(name=f"아이디 확인 결과", value=f"`{message.author.id}`가 {message.author.mention}님의 아이디에요!")
        embed.set_footer(text=message.author.name + " | Sky BOT#2208  스카이봇은 2명이 개발하고 있어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("/핑"):
        la = client.latency
        embed = discord.Embed(title="퐁!")
        embed.add_field(name="반응 속도", value=str(round(la * 1000)) + "ms")
        embed.set_footer(text=message.author.name + " | Sky BOT#2208  스카이봇은 2명이 개발하고 있어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("/계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                await message.channel.send("답: "+str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                await message.channel.send("답 : "+str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                await message.channel.send("답 : "+str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                await message.channel.send("답 : "+str(calcResult))
        except IndexError:
            await message.channel.send("무슨 숫자를 계산할지 알려주세요.")
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")

    if message.content.startswith("/도움말") or message.content.startswith("/명령어"):
        embed = discord.Embed(title="🔨ㅣSky BOT 도움말", timestamp=message.created_at,
        colour=discord.Colour.gold()
    )
        embed.add_field(name="/도움말, /명령어", value="스카이봇의 명령어 목록을 보여드려요!", inline=False)
        embed.add_field(name="/핑", value="스카이봇의 반응속도를 확인해요!", inline=False)
        embed.add_field(name="/계산 [더하기 / 빼기 / 곱하기 / 나누기] 숫자...", value="[더하기,뺴기,곱하기,나누기] 중에서 선택한 기호로 숫자... 를 계산해요! \n ( ex : /계산 더하기 1 1 ) ", inline=False)
        embed.add_field(name="/실검", value="네이버 실시간 검색어 순위를 확인해요!", inline=False)
        embed.add_field(name="/eval [내용]", value="cmd 겸용입니다. [내용] 에 해당하는 코드를 사용할 경우 반응하는 내용을 알려줍니다. \n ( ex : /eval import discord )", inline=False)
        embed.add_field(name="/코로나", value="국내 코로나 상황을 알려드려요!", inline=False)
        embed.add_field(name="/캡챠, /캡차", value="캡챠 인증코드가 생성된 후, 해당 인증코드를 작성하면 인증됩니다.")
        embed.add_field(name="〈 관리자 권한 필요 〉/청소 [청소할 메시지수]", value="[청소할 메시지수]에 해당하는 숫자만큼의 메시지를 삭제해요! \n ( 사용한 명령어 포함이므로 만약 3을 입력하면 실질적으로 2개가 삭제되는것과 같습니다. )", inline=False)
        embed.add_field(name="〈 관리자 권한 필요 〉/킥 [멘션]", value="[멘션]한 유저를 해당 서버에서 추방해요!", inline=False)
        embed.add_field(name="〈 관리자 권한 필요 〉/밴 [멘션]", value="[멘션]한 유저를 해당 서버에서 차단해요!", inline=False)
        embed.add_field(name="/피드백 [내용]", value="[내용]에 해당하는 메시지를 운영자에게 보냅니다.", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie#3907, 🍌🍭바나나🍭🍌#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content.startswith("/캡챠") or message.content.startswith("/캡차"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        embed = discord.Embed(title="인증코드", description = message.author.mention + ", 위에 있는 인증코드를 10초내에 입력해주세요.", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증시간 ( 10초 ) 를 초과했습니다.", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="성공!", description = message.author.mention + ", __**Captcha**__ 인증시간 내에 올바른 인증코드를 작성했습니다.", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await message.channel.send(embed=embed)
        
        else:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증코드가 올바르지 않습니다.", timestamp=message.created_at,
            colour=discord.Colour.red()
    )
            embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await message.channel.send(embed=embed)
        
       

    if message.content.startswith("/밴"):
        if message.author.guild_permissions.ban_members:
            userid = message.content[3:]
            user_id = re.findall("\d+", userid)
            userban = message.guild.get_member(int(user_id[0]))
            await message.guild.ban(userban)
            await message.channel.send(str(userban) + "님을 차단했어요!")
        else:
            await message.channel.send("권한이 부족해요!")

    if message.content.startswith("/킥"):
            if message.author.guild_permissions.kick_members:
                userid = message.content[3:]
                user_id = re.findall("\d+", userid)
                userkick = message.guild.get_member(int(user_id[0]))
                await message.guild.kick(userkick)
                await message.channel.send(str(userkick) + "님을 관리자 권한으로 추방했어요!")
            else:
                await message.channel.send("권한이 부족해요!")

    if message.content.startswith("/dm"):
        userdm = message.content[4:].split(",")
        getuser = userdm[0]
        getuserid = getuser[3:21]
        getusermention = client.get_user(int(getuserid))
        userdes = userdm[1]
        await getusermention.send(userdes)
        await message.channel.send("DM이 성공적으로 발송되었어요!")
 
    if message.content.startswith("/피드백"):
        Dansdml1 = message.content[5:]
        Dansdml = discord.Embed(title="**[ Sky BOT ]**", color=0x6777ff)
        Dansdml.add_field(name="• 문의하는 내용", value=f"{Dansdml1}\n\n• 문의하는 서버 : {message.guild.name}\n• 문의한 이용자 : {message.author.mention}", inline=False)
        Dansdml.set_thumbnail(url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
        Dansdml.set_footer(text=message.author , icon_url=message.author.avatar_url)
        m = await message.channel.send("문의발송 여부를 선택하여주세요.", embed=Dansdml)
        await m.add_reaction('✅')
        await m.add_reaction('❎')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
        except asyncio.TimeoutError:
            Drhdwltlrks = discord.Embed(title="**[ Sky BOT ]**", color=0xff0000)
            Drhdwltlrks.add_field(name="**문의**", value=f"{message.author.mention} **님 문의발송 선택 시간초과입니다.**", inline=False)
            Drhdwltlrks.set_thumbnail(url=message.author.avatar_url)
            Drhdwltlrks.set_footer(text="Sky BOT#2204" , icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await m.edit(content="문의발송이 취소되었습니다.", embed=Drhdwltlrks)
        else:
            if str(reaction.emoji) == "❎":
                Drhdwlcnlth = discord.Embed(title="**[ Sky BOT ]**", color=0xff0000)
                Drhdwlcnlth.add_field(name="**문의**", value=f"{message.author.mention} **님 문의발송이 취소되었습니다.**", inline=False)
                Drhdwlcnlth.set_thumbnail(url=message.author.avatar_url)
                Drhdwlcnlth.set_footer(text="Sky BOT#2204" , icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
                await m.edit(embed=Drhdwlcnlth)
            elif str(reaction.emoji) == "✅":
                await m.edit(content="서포트 서버에 피드백이 발송되었어요!", embed=Dansdml)
                await client.get_channel(int(736382917072257107)).send(embed=Dansdml)

    if message.content == "/실검":
        url = "https://m.search.naver.com/search.naver?query=%EC%8B%A4%EA%B2%80"
        html = urlopen(url)
        parse = BeautifulSoup(html, "html.parser")
        result = ""
        tags = parse.find_all("span", {"class" : "tit _keyword"})
        for i, e in enumerate(tags):
            result = result + (str(i+1))+"위 | "+e.text+"\n"
        await message.channel.send(result)

    if message.content.startswith("/공지"):
            if message.author.id in owner:
                if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                    await message.channel.send("공지로 사용할 메시지가 포함되지 않았습니다. 아래에 예시대로 시도하세요.")
                try:
                    msg = message.content[4:]
                    oksv = 0
                    embed = discord.Embed(
                        title = msg.split('&&')[0],
                        description = msg.split('&&')[1] + f"\n\n[스카이봇 서포트서버으로 이동하기!](https://discord.gg/egQBF2H)",
                        colour = discord.Colour.blue(),
                        timestamp = message.created_at
                    ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - Developer ● 봇 공지는 기본적으로 랜덤한 채널에 발송돼요!') .set_thumbnail(url=client.user.avatar_url_as(format=None, static_format="png", size=1024))
                except IndexError:
                    await message.channel.send("형식이 틀렸습니다. ``/공지 <제목>&&<내용>``으로 다시 시도해보세요.")
                m = await message.channel.send("아래와 같이 공지가 발신됩니다.", embed=embed)
                await m.add_reaction('✅')
                await m.add_reaction('❎')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
                except asyncio.TimeoutError:
                    await message.channel.send('시간이 초과되었습니다.')
                else:
                    if str(reaction.emoji) == "❎":
                        await message.channel.send("공지발신을 취소하였어요")
                    elif str(reaction.emoji) == "✅":
                        await m.edit(content="발신중입니다...", embed=embed)
                        for i in client.guilds:
                            arr = [0]
                            alla = False
                            flag = True
                            z = 0
                            for j in i.channels:
                                arr.append(j.id)
                                z+=1
                                if "ABOT-공지" in j.name or"봇-공지" in j.name or "봇_공지" in j.name or "봇공지" in j.name or "bot_announcement" in j.name or "공지" in j.name:
                                    if str(j.type)=='text':
                                        try:
                                            oksv += 1
                                            await j.send(embed=embed)
                                            alla = True
                                        except:
                                            pass
                                        break
                            if alla==False:
                                try:
                                    chan=i.channels[1]
                                except:
                                    pass
                                if str(chan.type)=='text':
                                    try:
                                        oksv += 1
                                        await chan.send(embed=embed)
                                    except:
                                        pass
                        await message.channel.send(f"**📢 공지 가 성공적으로 발신되었습니다. 📢**\n\n{len(client.guilds)}개의 서버 중에서  {oksv}개의 서버에 발신 완료했습니다., {len(client.guilds) - oksv}개의 서버에 발신 실패했습니다.")
                        await m.edit(content="발신이 완료되었습니다!", embed=embed)
            else:
                await message.channel.send('이 명령어를 쓰려면 최소 Bot Developer 권한이 필요합니다.') 

    if message.content.startswith("/청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[4:]
                await message.channel.purge(limit=int(amount))
                embed = discord.Embed(title="청소 완료!", description=f"{message.author.mention}, **{amount}** 개의 메시지를 청소했어요!", timestamp=message.created_at,
                colour = discord.Colour.green()
    )
                embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736130989109280812/736134727639105577/skybot.png")
                await message.channel.send(embed=embed)
            except ValueError:
                embed = discord.Embed(title="청소 실패!", description=f"{message.author.mention}, 청소할 메시지가 정해져 있지 않아요!", timestamp=message.created_at, 
                colour=discord.Colour.orange()
    )
                embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736130989109280812/736134727639105577/skybot.png")
                await message.channel.send(embed=embed)
        else:
                embed = discord.Embed(title="청소 실패!", description=f"{message.author.mention}, 청소를 실행할 권한이 부족해요!", timestamp=message.created_at, 
                colour=discord.Colour.red()
    )
                embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736130989109280812/736134727639105577/skybot.png")
                await message.channel.send(embed=embed)

    if message.content.startswith('/eval'):
        try:
            cmd = message.content[6:]
            output = eval(cmd)
            await message.channel.send(output)
        except:
            await message.channel.send("오류가 발생했습니다.")
            

    if message.content.startswith("/코로나"):
        # 보건복지부 코로나 바이러스 정보사이트"
        covidSite = "http://ncov.mohw.go.kr/index.jsp"
        covidNotice = "http://ncov.mohw.go.kr"
        html = urlopen(covidSite)
        bs = BeautifulSoup(html, 'html.parser')
        latestupdateTime = bs.find('span', {'class': "livedate"}).text.split(',')[0][1:].split('.')
        statisticalNumbers = bs.findAll('span', {'class': 'num'})
        beforedayNumbers = bs.findAll('span', {'class': 'before'})

        #주요 브리핑 및 뉴스링크
        briefTasks = []
        mainbrief = bs.findAll('a',{'href' : re.compile('\/tcmBoardView\.do\?contSeq=[0-9]*')})
        for brf in mainbrief:
            container = []
            container.append(brf.text)
            container.append(covidNotice + brf['href'])
            briefTasks.append(container)
        print(briefTasks)

        # 통계수치
        statNum = []
        # 전일대비 수치
        beforeNum = []
        for num in range(7):
            statNum.append(statisticalNumbers[num].text)
        for num in range(4):
            beforeNum.append(beforedayNumbers[num].text.split('(')[-1].split(')')[0])

        totalPeopletoInt = statNum[0].split(')')[-1].split(',')
        tpInt = ''.join(totalPeopletoInt)
        lethatRate = round((int(statNum[3]) / int(tpInt)) * 100, 2)
        embed = discord.Embed(title="Covid-19 통계", description="",color=0x5CD1E5)
        embed.add_field(name="데이터 제공", value="http://ncov.mohw.go.kr/index.jsp", inline=False)
        embed.add_field(name="마지막 수정일",value="해당 자료는 " + latestupdateTime[0] + "월 " + latestupdateTime[1] + "일 "+latestupdateTime[2] +"자료에요!", inline=False)
        embed.add_field(name="확진환자(누적)", value=statNum[0].split(')')[-1]+"("+beforeNum[0]+")",inline=True)
        embed.add_field(name="완치환자(격리해제)", value=statNum[1] + "(" + beforeNum[1] + ")", inline=True)
        embed.add_field(name="치료중(격리 중)", value=statNum[2] + "(" + beforeNum[2] + ")", inline=True)
        embed.add_field(name="사망", value=statNum[3] + "(" + beforeNum[3] + ")", inline=True)
        embed.add_field(name="누적확진률", value=statNum[6], inline=True)
        embed.add_field(name="치사율", value=str(lethatRate) + " %",inline=True)
        embed.add_field(name=": 최신 브리핑 1 : " + briefTasks[0][0],value="Link : " + briefTasks[0][1],inline=False)
        embed.add_field(name=": 최신 브리핑 2 : " + briefTasks[1][0], value="Link : " + briefTasks[1][1], inline=False)
        embed.set_thumbnail(url="https://wikis.krsocsci.org/images/7/79/%EB%8C%80%ED%95%9C%EC%99%95%EA%B5%AD_%ED%83%9C%EA%B7%B9%EA%B8%B0.jpg")
        embed.set_footer(text='해당 자료는 J-hoplin님의 소스코드를 이용했습니다.', 
                        icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
        await message.channel.send("코로나 19의 통계 Embed 입니다.", embed=embed)

client.run('Token')
