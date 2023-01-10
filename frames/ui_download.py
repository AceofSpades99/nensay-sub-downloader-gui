# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_download.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import webbrowser
import os
from pathlib import Path

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
from bs4 import BeautifulSoup

from modules import download_script
from modules.download_script import Chapter, CustomException

current_anime_page = 1
current_ch_page = 1
search_text = ""
chosen_anime = ""
search_query = []
chapters = []
client = requests.Session()


class Ui_Download_Dialog(QDialog):

    def setupUi(self, Download_Dialog):
        global client
        Download_Dialog.setObjectName("Download_Dialog")
        Download_Dialog.resize(722, 535)
        self.exit_btn = QtWidgets.QPushButton(Download_Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(470, 470, 161, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.plainTextEdit = QtWidgets.QLineEdit(Download_Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(290, 20, 391, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.chapters_label = QtWidgets.QLabel(Download_Dialog)
        self.chapters_label.setGeometry(QtCore.QRect(470, 50, 131, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(17)
        self.chapters_label.setFont(font)
        self.chapters_label.setObjectName("chapters_label")
        self.search_label = QtWidgets.QLabel(Download_Dialog)
        self.search_label.setGeometry(QtCore.QRect(40, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.search_label.setFont(font)
        self.search_label.setObjectName("search_label")
        self.chapter_list = QtWidgets.QListView(Download_Dialog)
        self.chapter_list.setGeometry(QtCore.QRect(390, 110, 311, 311))
        self.chapter_list.setObjectName("chapter_list")
        self.dl_btn = QtWidgets.QPushButton(Download_Dialog)
        self.dl_btn.setGeometry(QtCore.QRect(90, 470, 161, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.dl_btn.setFont(font)
        self.dl_btn.setObjectName("dl_btn")
        self.loadChaptersBtn = QtWidgets.QPushButton(Download_Dialog)
        self.loadChaptersBtn.setGeometry(QtCore.QRect(340, 230, 41, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        self.loadChaptersBtn.setFont(font)
        self.loadChaptersBtn.setObjectName("loadChaptersBtn")
        self.query_list = QtWidgets.QListView(Download_Dialog)
        self.query_list.setGeometry(QtCore.QRect(20, 110, 311, 311))
        self.query_list.setObjectName("query_list")
        self.search_btn = QtWidgets.QPushButton(Download_Dialog)
        self.search_btn.setGeometry(QtCore.QRect(190, 20, 91, 31))
        self.search_btn.setObjectName("search_btn")
        self.label_2 = QtWidgets.QLabel(Download_Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.n_page_anime = QtWidgets.QPushButton(Download_Dialog)
        self.n_page_anime.setGeometry(QtCore.QRect(220, 430, 75, 23))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.n_page_anime.setFont(font)
        self.n_page_anime.setObjectName("n_page_anime")
        self.n_page_anime.setDisabled(True)
        self.p_page_anime = QtWidgets.QPushButton(Download_Dialog)
        self.p_page_anime.setGeometry(QtCore.QRect(50, 430, 81, 23))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.p_page_anime.setFont(font)
        self.p_page_anime.setObjectName("p_page_anime")
        self.p_page_anime.setDisabled(True)
        self.p_page_chapter = QtWidgets.QPushButton(Download_Dialog)
        self.p_page_chapter.setGeometry(QtCore.QRect(420, 430, 81, 23))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.p_page_chapter.setFont(font)
        self.p_page_chapter.setObjectName("p_page_chapter")
        self.p_page_chapter.setDisabled(True)
        self.n_page_chapter = QtWidgets.QPushButton(Download_Dialog)
        self.n_page_chapter.setGeometry(QtCore.QRect(600, 430, 75, 23))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.n_page_chapter.setFont(font)
        self.n_page_chapter.setObjectName("n_page_chapter")
        self.n_page_chapter.setDisabled(True)
        self.dl_btn.setDisabled(True)
        download_script.login(client)

        self.retranslateUi(Download_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Download_Dialog)

    def retranslateUi(self, Download_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Download_Dialog.setWindowTitle(_translate("Download_Dialog", "Dialog"))
        self.exit_btn.setText(_translate("Download_Dialog", "EXIT"))
        self.chapters_label.setText(_translate("Download_Dialog", "Chapters"))
        self.search_label.setText(_translate("Download_Dialog", "Search an anime:"))
        self.dl_btn.setText(_translate("Download_Dialog", "Download (Save as)"))
        self.loadChaptersBtn.setText(_translate("Download_Dialog", ">>"))
        self.search_btn.setText(_translate("Download_Dialog", "Search"))
        self.label_2.setText(_translate("Download_Dialog", "Anime Results"))
        self.n_page_anime.setText(_translate("Download_Dialog", "Next page"))
        self.p_page_anime.setText(_translate("Download_Dialog", "Prev. page"))
        self.p_page_chapter.setText(_translate("Download_Dialog", "Prev. page"))
        self.n_page_chapter.setText(_translate("Download_Dialog", "Next page"))

    def change_page(self, listType, direction):
        """
        Changes desired QtlistView to another page if available

        :param listType: 'anime' for Anime names list, 'chapters' for chapters names list
        :param direction: 'previous' loads previous page from chosen list, 'next' loads next page from chosen list

        """
        global search_query, chapters, current_anime_page, current_ch_page
        try:
            if listType == 'anime':
                url = f"http://nensaysubs.net/buscador/?query={search_text.replace(' ', '+')}&pn={current_anime_page}"
                with client.post(url) as response:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    if direction == 'next':
                        current_anime_page += 1
                        new_page = soup.find(name='a', text='Siguiente').get('href')
                    elif direction == 'previous':
                        current_anime_page -= 1
                        new_page = soup.find(name='a', text='Anterior').get('href')
                with client.get(new_page) as response:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    search_query = download_script.reload_filter(soup)
                    self.__set_list_model('anime')
            else:
                url = f"http://nensaysubs.net/sub/{chosen_anime.replace(' ', '_')}&pn={current_ch_page}"
                with client.post(url) as response:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    if direction == 'next':
                        current_ch_page += 1
                        new_page = soup.find(name='a', text='Siguiente').get('href')
                    elif direction == 'previous':
                        current_ch_page -= 1
                        new_page = soup.find(name='a', text='Anterior').get('href')
                with client.get(new_page) as response:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    chapters = download_script.reload_chapters(soup)
                    self.__set_list_model('chapters')
        except ConnectionError:
            message = QtWidgets.QMessageBox()
            message.setText('There has been a connection error')
            message.setWindowTitle('Error')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()

    def __set_list_model(self, listType):
        """
        Sets a model for one of the two QtListViews

        :param listType: 'anime' for Anime names list, 'chapters' for chapters names list

        """
        if listType == 'anime':
            list = search_query
            listView = self.query_list
            prev_btn = self.p_page_anime
            next_btn = self.n_page_anime
            prev_flag = download_script.prev_anime
            next_flag = download_script.next_anime
        else:
            list = chapters
            listView = self.chapter_list
            prev_btn = self.p_page_chapter
            next_btn = self.n_page_chapter
            prev_flag = download_script.prev_chapter
            next_flag = download_script.next_chapter
        model = QtGui.QStandardItemModel()
        for item in list:
            entry = QtGui.QStandardItem(item) if not isinstance(item, Chapter) else QtGui.QStandardItem(item.title)
            model.appendRow(entry)
        listView.setModel(model)
        prev_btn.setEnabled(True) if prev_flag else prev_btn.setDisabled(True)
        next_btn.setEnabled(True) if next_flag else next_btn.setDisabled(True)

    def search_anime(self):
        """
        Searchs for input anime in the web using search func from download_script and fills the list with its reults

        """
        global search_text, search_query, client, current_anime_page
        current_anime_page = 1
        try:
            print("done")
            print(self.plainTextEdit.text())
            search_text = self.plainTextEdit.text()
            search_query = download_script.search(client, search_text)
            print(search_query)
            self.__set_list_model('anime')
        except CustomException as e:
            message = QtWidgets.QMessageBox()
            message.setText(e.message)
            message.setWindowTitle('Error')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()
        except ConnectionError:
            message = QtWidgets.QMessageBox()
            message.setText('There has been a connection error')
            message.setWindowTitle('Error')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()


    def load_chapters(self):
        """
        Retrieves all chosen anime's chapters for first page using get_chapters func from download_script and fills chapters list

        """
        global chapters, chosen_anime, current_ch_page
        try:
            current_ch_page = 1
            index = int(self.query_list.currentIndex().row())
            print(index)
            chosen_anime = search_query[index]
            print(chosen_anime)
            chapters = download_script.get_chapters(client, chosen_anime)
            self.__set_list_model('chapter')
            self.dl_btn.setEnabled(True)
        except ConnectionError:
            message = QtWidgets.QMessageBox()
            message.setText('There has been a connection error')
            message.setWindowTitle('Error')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()

    def download_sub(self):
        """
        Downloads chosen subtitle file in selected location, user must submit correct captcha code to avoid file data corruption

        """
        global chapters, client
        try:
            index = int(self.chapter_list.currentIndex().row())
            zip_name = chapters[index].title.replace(':', '')
            link = chapters[index].link
            dl_link = f'https://nensaysubs.net/{link}'
            print(zip_name)
            print(dl_link)
            with client.get(dl_link):
                with client.get('http://nensaysubs.net/senos/seguro.php') as pic:
                    chunk = pic.content
                    message = QtWidgets.QMessageBox(parent=self)
                    message.setText('You will be sent a picture with a code, please save it and type it in the next window')
                    message.setWindowTitle('Info')
                    message.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    message.exec_()
                    with open('photo.png', 'wb') as file:
                        file.write(chunk)
                    webbrowser.open('photo.png')
                    code, option = QtWidgets.QInputDialog.getText(self, 'Send code',
                                                             'Send opened picture code, if entered wrong zip will be corrupt')
                    if not option:
                        os.remove('photo.png')
                        return
                    print(code)
                    with client.post('http://nensaysubs.net/solicitud/', data={'code': code.lower()}) as dl:
                        chunk = dl.content
                        save_path = QFileDialog.getExistingDirectory(parent=self,
                                                                     caption='Select where do you want to save the file')
                        print(save_path)
                        if save_path == "":
                            save_path = Path.home() / "Downloads"
                        full_path = os.path.join(save_path, f'{zip_name}.zip')
                        full_path = os.path.abspath(full_path)
                        with open(full_path, 'wb') as file:
                            file.write(chunk)
                        message = QtWidgets.QMessageBox(parent=self)
                        message.setText(f'Saved succesfully at {full_path}')
                        message.setWindowTitle('Success')
                        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        message.show()
                    os.remove('photo.png')
        except ConnectionError:
            message = QtWidgets.QMessageBox()
            message.setText('There has been a connection error')
            message.setWindowTitle('Error')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()
        except:
            message = QtWidgets.QMessageBox()
            message.setText('We cannot determine the source of the error, try again')
            message.setWindowTitle('Error')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()
