# -*- coding: utf-8 -*-
import scrapy
import browsercookie
import pyautogui as gui
from datetime import datetime
from threading import Timer
from scrapy_splash import SplashRequest


start_script = '''
function main(splash, args)
  splash:go("https://ppt.mfa.gov.cn/appom/")
  splash:wait(2.5)
  continue =splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div.menuList > a:nth-child(2)")   continue:mouse_click()
  splash:wait(1)
  banko = splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div:nth-child(8) > div > table > tr:nth-child(1) > td > a > div.mint-cell-wrapper > div.mint-cell-value")
  banko:send_text('档案号')
  question_list = splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div:nth-child(8) > div > table > tr:nth-child(2) > td > a > div.mint-cell-wrapper > div.mint-cell-value > input")
  question_list:mouse_click()
  splash:wait(1)
  question = splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div:nth-child(7) > div > ul > a:nth-child(2) > div.mint-cell-wrapper")
  question:mouse_click()
  splash:wait(1)
  answer = splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div:nth-child(8) > div > table > tr:nth-child(3) > td > a > div.mint-cell-wrapper > div.mint-cell-value > input")
  answer:send_text('回答')
  splash:wait(1)
  submit = splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div:nth-child(8) > div > button:nth-child(4)")
  submit:mouse_click()
  splash:wait(2)
  inter = splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div > div.bottom_bths > button")
  inter:mouse_click()
  splash:wait(3)
  kakunin = splash:select("#app > div > div.page-wrap > div > div > div:nth-child(1) > div > div.mint-popup.tipPopup.mint-popup-center > div > button") 	
  splash:wait(2)
  kakunin:mouse_click()	
  splash:wait(1)
  return {
    html=splash:html(),
  }
end
'''
class AppointementSpider(scrapy.Spider):
    name = 'appointement'
    start_urls = ['https://ppt.mfa.gov.cn/appom/']

    cookie_k = []
    cookie_v = []
    for cookie in browsercookie.chrome():
        if ('ppt.mfa.gov.cn'.rfind(str(cookie.domain)) != -1):
            cookie_k.append(cookie.name)
            cookie_v.append(cookie.value)
    cookies = dict(zip(cookie_k, cookie_v))
    print(cookies)

    def start_requests(self):
        print("开始")
        yield SplashRequest(url=self.start_urls[0],callback=self.parse,endpoint='execute',args={
            'lua_source': start_script
        })
        print("请求了")

    def parse(self, response):
        mouth = response.xpath("//*[@id='app']/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[contains(@class,'events-week')]/div[contains(@class,'today2')]/div/p/text()").extract()
        i = 0
        for week in mouth:
            week = week.strip()
            week = week[0:2]
            print(week)
            if int(week) < 50 :
              x, y = gui.position()
              gui.click(x=x, y=y, button='left')
              gui.typewrite('you can make a reservation !!! GO!GO!GO!')
              gui.hotkey('enter')
              gui.typewrite('you can make a reservation !!! GO!GO!GO!')
              gui.hotkey('enter')
              gui.typewrite('you can make a reservation !!! GO!GO!GO!')
              gui.hotkey('enter')
        # print("返回了")

