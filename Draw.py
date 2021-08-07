from PIL import Image, ImageFont, ImageDraw

from weatherTools import get_mainData, get_lifeStyle
import numpy as np

class Draw():
    def __init__(self):
        self.fontSize_title = 40
        self.fontSize_text = 30
        self.title_color = '#00ff00'
        font_path = r"font/simsun.ttc"
        self.font_title = ImageFont.truetype(font_path, self.fontSize_title)
        self.font_text = ImageFont.truetype(font_path, self.fontSize_text)

    def clac_size(self,text):
        lines = text.split('\n')
        num = []
        for i in lines:
            if i != '':
                num.append(len(i))
        nums = np.array(num)
        width = nums.max()
        height = len(lines)+2
        # print('width: ', width)
        # print('height: ', height)
        return width,height

    def CreateImg(self, filename, text):

        lines = text.split('\n')

        size = self.clac_size(text)

        img = Image.new("RGB", (size[0]*30, size[1]*30), (0, 0, 0))
        pos = [0, 0]
        for i in lines:


            if i != '':
                temp=i.split(':')
                self.render(img=img, font_type='title', font_color=self.title_color, pos=pos, text=temp[0]+':')
                pos[0]=len(temp[0])*40+15
                pos[1]+=40
                self.render(img=img, font_type='text', font_color='#FFFFFF', pos=pos, text=temp[1])
                pos[0]=0

        # dr = ImageDraw.Draw(img)
        #
        # dr.text((0, 0), text, font=self.font_title, fill="#00FF00")
        # img.save('{}.png'.format(filename))
        self.save_toFile(img, filename)
        # img.show()

    def render(self, img,font_type, font_color, pos, text):
        drawer = ImageDraw.Draw(img)
        if font_type == 'title':
            drawer.text((pos[0], pos[1]), text, font=self.font_title, fill=font_color)
        else:
            drawer.text((pos[0], pos[1]-30), text, font=self.font_text, fill=font_color)
        pass

    def save_toFile(self, img, filename):
        img.save('images/{0}.png'.format(filename))

if __name__ == '__main__':
    pt1 = get_mainData('str')
    pt2 = get_lifeStyle('str')
    init = Draw()
    init.CreateImg('test', pt2)