from telegram.ext import Dispatcher
from lib2to3.pgen2 import token
import telegram
from telegram.ext import Updater #저장
from telegram.ext import CommandHandler, CallbackQueryHandler #디스패쳐가 수행할 이벤트를 정의하는 클래스
from telegram import InlineKeyboardButton as BT, ReplyMarkup #버튼
from telegram import InlineKeyboardMarkup as MU #버튼을 감싸는 마크업
import os

# 텔레그램 봇 만들것임
# 여러 도박성 게임을 만들것
# 숫자게임, 가위바위보 등등
# 배당 조정해놓고할것
# 본인의 id = 지갑주소로 할것
# mysql 지갑주소를 연동하여 db생성
# 출금은 id 로만 보낼것

#7년차 마케팅봇 토큰
token ='5393373488:AAEed3YfXQOKhQG52emlMnlU7DUDr6Es8EA'

#봇설정
bot = telegram.Bot(token=token)

#updater , dispatcher 설정 사용자와 업데이터가 서로 정보를 주고받고
#업데이터가 A에 저장. A에 저장한것을 디스패쳐가 가져옴
#디스패쳐가 저장한것을 가져오고 그에맞는 함수를 불러서
#사용자에게 보냄.
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

#모든사용자 설정

#버튼생성
btn1 = BT(text = '🔔[HOT] 계정 상점', callback_data='1')
btn2 = BT(text = '🔔 계정 생성프로그램', callback_data= '2')
btn3 = BT(text = '🔔 각종프로그램제작', callback_data= '3')
btn4 = BT(text = '🔔 [HOT] 맘카페 자동가입,등업', callback_data= '4')
btn5 = BT(text = '🔔 [HOT] 트위터 무한게시', callback_data= '5')
btn6 = BT(text = '🔔 [HOT] 구글 상위 노출', callback_data= '6')
btn7 = BT(text = '🔔 카톡 오픈방 상위 노출', callback_data= '7')
btn8 = BT(text = '🔔 해외유심 상점', callback_data= '8')
btn9 = BT(text = '🔔 [HOT] 인스타 DM 발송', callback_data= '9')
btn10 = BT(text = '🔔 코인 결제 하는 방법', callback_data= '10')


btn_start = BT(text = '처음으로 돌아가기', callback_data= 'goback')


#마크업생성
mu = MU(inline_keyboard = [[btn1], [btn2], [btn3], [btn4], [btn5], [btn6], [btn7], [btn8], [btn9], [btn10]])# 세로배열
# mu1 = MU(inline_keyboard = [[btn1_1], [btn_start]])# 리스트 + 처음으로돌아가기버튼
# mu2 = MU(inline_keyboard = [[btn2_1], [btn_start]])# 리스트 + 처음으로돌아가기버튼
# mu3 = MU(inline_keyboard = [[btn3_1], [btn_start]])# 리스트 + 처음으로돌아가기버튼
# mu4 = MU(inline_keyboard = [[btn4_1], [btn_start]])# 리스트 + 처음으로돌아가기버튼
# mu5 = MU(inline_keyboard = [[btn5_1], [btn_start]])# 리스트 + 처음으로돌아가기버튼

mu_start = MU(inline_keyboard = [[btn_start]])# 처음으로 돌아가기버튼만 생성

text_accs = '🔔        계정 상점        🔔\n\n\
📣 모든 거래는 코인으로 거래합니다.\n\
📣 경쟁업체의 방해로 인하여 거래방식 변경합니다\n\
📣 모든 계정은 대량구매시 대폭할인 들어갑니다 ^^\n\
📣 키핑시스템 가능 (ex: 100개 구매후 필요할때만 가져가기)\n\
📣 최소 10개단위로 판매중\n\n\
🔴 트위터 계정\n\
💲 공계정 = 개당 5000원\n\n\
공계정 외 다른 조건 계정은 문의주세요.\n\n\
🔴 인스타 계정\n\
💲 공계정 = 개당 4000원\n\n\
공계정 외 다른 조건 계정은 문의주세요.\n\n\
🔴 페북 계정\n\
💲 공계정 = 개당 7000원\n\n\
공계정 외 다른 조건 계정은 문의주세요.\n\n\
🔴 네이버 계정\n\
💲 비실명계정 = 개당 10000원\n\
💲 맘카페계정(약 200개이상의 카페가입완료) = 개당 20만원 \n\
📣 최소 1개부터 구매가능\n\n\
🔴 카카오톡 계정\n\
💲 pc버전 = 개당 40000원\n\
💲 모바일 = 개당 70000원\n\
📣 최소 1개부터 구매가능\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
'
text_accp = '🔔     계정 생성프로그램     🔔\n\n\
📣 직접 sns나 포털사이트 가입 가능합니다.\n\
📣 계정 구매보다 더 저렴한 비용으로 생성가능\n\
📣 충전식이므로 언제든 사용가능 ^^\n\n\
💲 프로그램 비용 = 10만원\n\
💲 가상번호 1개당 = 1000원\n\n\
🔴 대량구매시 번호당 500원까지 할인가능\n\
🔴 인증번호가 날라오지 않을시 요금차감 X\n\
🔴 네이버,구글,트위터,인스타,페북 등 사용가능!\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
text_program = '🔔      프로그램제작     🔔\n\n\
📣 원하시는 프로그램을 제작해드립니다.\n\
📣 상세한 프로그램의 기능을 전달해주세요.\n\
📣 가능여부와 견적을 뽑아서 답변드리겠습니다.\n\n\
💲 비용 = 문의후 견적요청.\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
text_momcafe = '🔔      맘카페 대행      🔔\n\n\
📣 바이럴 마케팅 하시는 사장님들이나 이제 새로 맘카페 바이럴마케팅을 해보시려는분들에게 필수 ! !\n\
📣 약 300개의 카페에 자동가입 + 자동댓글 + 자동출석 까지 다해드립니다.\n\
📣 300개인 이유 = 계정당 최대 300개의 카페가입가능\n\
📣 계정 1개기준 카페가입시도 300개 + 등업을위한 댓글,출석 < 언제다합니까?!\n\
📣 계정 10개기준 일주일안으로 마무리 해드립니다 ^^\n\n\
🔴 손님이 계정 준비해왔을 경우\n\
💲 계정당 비용 = 10만원(가입)\n\
💲 계정당 비용 = 15만원(가입,댓글,출석)\n\n\
🔴 손님이 계정 없을 경우\n\
💲 맘카페계정 + 카페가입 + 댓글 + 출석 = 20만원\n\
📣 계정만 따로 판매하지는 않습니다. 무조건 가입된계정만 판매중입니다 ^^\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
text_twitter = '🔔     트위터 무한트윗게시     🔔\n\n\
📣 트위터, 카톡, 인스타, 구글 보고 오신분들이죠?!\n\
📣 그만큼 효과가 좋습니다 무한트윗 ^^\n\
📣 구글 상위에 노출되는 효과까지 보실수있습니다.\n\
📣 365일 매시간마다 트윗합니다 ~ ^^\n\n\
🔴 무한 트윗\n\n\
💲 90일 = 50만원\n\
💲 180일 = 90만원\n\
💲 1년 = 150만원\n\n\
❗ 계정 최대 50개까지 설정가능\n\
❗ 계정 1개당 딜레이를 1시간으로 잡을 시 1시간안에 50개의 트윗이 올라갑니다 ^^\n\
❗ 신청하신 기간동안 올라갑니다 !\n\
❗ 계정은 별도로 필요합니다.(필요시 저희업체에서 구매가능)\n\
❗ 도배로 인한 계정 정지시 추가 가능\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
text_google = '🔔     구글 상위 노출     🔔\n\n\
📣 고품질 백링크 + 트래픽으로 상위노출\n\
📣 모든 키워드 가능합니다.\n\
📣 키워드 갯수 = 5~10개\n\
📣 준비물 = 랜딩사이트\n\n\
💲 월 관리형 패키지 A = 50만원\n\
💎 고품질백링크 5000개 + 고품질트래픽 10000개\n\n\
💲 월 관리형 패키지 B = 90만원\n\
💎 고품질백링크 10000개 + 고품질트래픽 20000개 + DA점수(도메인점수) 상승\n\n\
💲 월 관리형 패키지 C = 150만원\n\
💎 고품질백링크 20000개 + 고품질트래픽 40000개 + DA점수(도메인점수) 상승 + 피라미드 백링크 구축 (백링크에 백링크를 심는 체계적인 구축 효과 UP)\n\n\
💲 월 유지형 패키지 = 30만원\n\
💎 고품질백링크 3000개 + 고품질트래픽 5000개 ( 순위 유지를 위한 상품 )\n\n\
🔴 월결제가 부담스러우신분들은 따로문의주세요 ^^\n\
🔴 원하시는 방향을 말씀해주시면 맞춰드리겠습니다 !\n\
🔴 백링크란? 랜딩페이지(실제 손님들이 도달하는 사장님의 홈페이지)의 도메인 주소를 외부에서 많이 언급하여 인기 상승 시켜서 구글상위노출 시킵니다.\n\
🔴 이 분야 전문가 입니다. 믿고 맡겨주시면 보답하겠습니다 ^^\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
text_kakaotalk = '🔔        카카오톡        🔔\n\n\
📣 카카오톡 상위노출( 하트작업 + 인원작업 + seo기법 )\n\
📣 카카오톡 계정 ( 해외계정 )\n\n\
💲 인원작업 = 1명당 1500원\n\
💲 인원 + 하트 = 1명당 2000원\n\
💎 대량 구매시 할인 들어갑니다 ^^\n\n\
🔴 카카오톡 계정\n\
💲 pc버전 = 개당 40000원\n\
💲 모바일 = 개당 70000원\n\
💎 대량 구매시 할인 들어갑니다 ^^\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
text_usim = '🔔        해외유심        🔔\n\n\
📣 하나의 유심으로 모든 인증번호 받을수있습니다.\n\
📣 요금충전시 실제로 문자 전화도 가능합니다 ^^\n\
📣 해외 현지 유심으로 100% 합법 유심입니다.(대기업도씀)\n\
📣 수요가 많은 상황은 아니라 꼭 필요하신분만 연락주세요\n\n\
💲 유심가격 = 개당 10000원(요금충전 별도 안해도됩니다.)\n\
💲 50개이상 = 개당 9000원\n\
💲 100개이상 = 개당 8000원\n\
💲 500개이상 = 개당 6000원\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
text_instadm = '🔔     인스타DM 발송대행     🔔\n\n\
📣 원하시는 해시태그 타겟 !\n\
📣 요즘 누가 db문자 발송하나요?!\n\
📣 DM 마케팅 효과 더욱 높습니다 ^^\n\n\
💲 건당 = 100원 ( 대량구매시 가격 합의가능 )\n\
❗ 적당한 속도로 꾸준히 보내드립니다 ^^(스팸방지용)\n\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'

text_btc = '🔔     코인결제 방법     🔔\n\n\
📣 비트코인, 리플, 이더리움 등 많은 방법으로 구매가능\n\
📣 가상화폐 거래소에 원화 충전후 코인구매\n\
📣 구매한 코인을 거래할 지갑으로 전송\n\
📣 판매자는 확인후 상품을 지급합니다.\n\n\
🔴 코인거래 정말 쉽고 편리합니다.\n\
🔴 코인거래하는 이유는 계좌거래시 경쟁업체에서 방해를 합니다.\n\
🔴 서로의 안전을 위하여 코인거래 하는겁니다 ^_^\n\
❗ 위 방법대로도 못하겠으면 코인 대행구매 알아봐드립니다.\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n\
📞 문의 : @goat82 < 클릭\n'
#/START 라고 보낼시 HELLOWORLD 라는 말을보냄
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='📣 안녕하세요 여러분 GOAT 입니다.\n\n🔔 마케팅에 꼭 ! 필요하신것들만 모아놨습니다.\n🔔 가격정보, 자주하는 질문, 정리다해놨습니다.\n🔔 원활한 소통을 위하여 읽어주시고 문의주세요 ^^ \n\n 🔔 문의 : @goat82', reply_markup = mu)

start_handler = CommandHandler('start', start)

#각 이벤트에 대한 Command Handler 생성.
#CommandHandler("명령어", Callback def {start})
def btn_callback(update, context):
    query = update.callback_query
    print(update.effective_chat.id, query.data)
    # query.answer('selected: {}'.format(query.data))
    if query.data == '1': #만약 콜백데이터가 1 일때 이렇게하라.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_accs, reply_markup = mu_start)
    elif query.data =='2': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_accp, reply_markup = mu_start)
    elif query.data =='3': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_program, reply_markup = mu_start)
    elif query.data =='4': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_momcafe, reply_markup = mu_start)
    elif query.data =='5': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_twitter, reply_markup = mu_start)
    elif query.data =='6': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_google, reply_markup = mu_start)
    elif query.data =='7': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_kakaotalk, reply_markup = mu_start)
    elif query.data =='8': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_usim, reply_markup = mu_start)
    elif query.data =='9': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_instadm, reply_markup = mu_start)
    elif query.data =='10': #만약 콜백데이터가 2 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_btc, reply_markup = mu_start)
    elif query.data =='goback': #만약 콜백데이터가 11 일때.
        context.bot.send_message(chat_id=update.effective_chat.id, text='📣 안녕하세요 여러분 GOAT 입니다.\n\n🔔 마케팅에 꼭 ! 필요하신것들만 모아놨습니다.\n🔔 가격정보, 자주하는 질문, 정리다해놨습니다.\n🔔 원활한 소통을 위하여 읽어주시고 문의주세요 ^^ \n\n 🔔 문의 : @goat82', reply_markup = mu)
callback_handler = CallbackQueryHandler(btn_callback)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(callback_handler)


print('starting...')
# Handler를 Dispatcher에 추가.
updater.start_polling()
# Updater가 메시지를 계속 감시.
updater.idle()
# 신호 중 하나가 수신 될 때까지 차단하고 업데이터를 중지.

