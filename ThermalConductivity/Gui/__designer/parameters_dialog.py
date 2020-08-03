/********************************************************************************
** Form generated from reading UI file 'parameters_dialog.ui'
**
** Created by: Qt User Interface Compiler version 5.15.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PARAMETERS_DIALOG_H
#define PARAMETERS_DIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>

QT_BEGIN_NAMESPACE

class Ui_Dialog_Parameters
{
public:
    QGridLayout *gridLayout_2;
    QDialogButtonBox *buttonBox;
    QGridLayout *gridLayout;
    QLabel *label_6;
    QLabel *label_2;
    QLabel *label_3;
    QComboBox *comboBox_symmetrize;
    QComboBox *comboBox_forceKxy;
    QLineEdit *lineEdit_width;
    QLabel *label_5;
    QComboBox *comboBox_sign;
    QLineEdit *lineEdit_length;
    QLabel *label_4;
    QLineEdit *lineEdit_thickness;
    QLabel *label;
    QLineEdit *lineEdit_gain;
    QLabel *label_7;

    void setupUi(QDialog *Dialog_Parameters)
    {
        if (Dialog_Parameters->objectName().isEmpty())
            Dialog_Parameters->setObjectName(QString::fromUtf8("Dialog_Parameters"));
        Dialog_Parameters->resize(400, 300);
        gridLayout_2 = new QGridLayout(Dialog_Parameters);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        buttonBox = new QDialogButtonBox(Dialog_Parameters);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout_2->addWidget(buttonBox, 1, 0, 1, 1);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_6 = new QLabel(Dialog_Parameters);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout->addWidget(label_6, 5, 0, 1, 1);

        label_2 = new QLabel(Dialog_Parameters);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        label_3 = new QLabel(Dialog_Parameters);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        comboBox_symmetrize = new QComboBox(Dialog_Parameters);
        comboBox_symmetrize->addItem(QString());
        comboBox_symmetrize->addItem(QString());
        comboBox_symmetrize->setObjectName(QString::fromUtf8("comboBox_symmetrize"));

        gridLayout->addWidget(comboBox_symmetrize, 4, 1, 1, 1);

        comboBox_forceKxy = new QComboBox(Dialog_Parameters);
        comboBox_forceKxy->addItem(QString());
        comboBox_forceKxy->addItem(QString());
        comboBox_forceKxy->setObjectName(QString::fromUtf8("comboBox_forceKxy"));

        gridLayout->addWidget(comboBox_forceKxy, 5, 1, 1, 1);

        lineEdit_width = new QLineEdit(Dialog_Parameters);
        lineEdit_width->setObjectName(QString::fromUtf8("lineEdit_width"));

        gridLayout->addWidget(lineEdit_width, 0, 1, 1, 1);

        label_5 = new QLabel(Dialog_Parameters);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 4, 0, 1, 1);

        comboBox_sign = new QComboBox(Dialog_Parameters);
        comboBox_sign->addItem(QString());
        comboBox_sign->addItem(QString());
        comboBox_sign->setObjectName(QString::fromUtf8("comboBox_sign"));

        gridLayout->addWidget(comboBox_sign, 3, 1, 1, 1);

        lineEdit_length = new QLineEdit(Dialog_Parameters);
        lineEdit_length->setObjectName(QString::fromUtf8("lineEdit_length"));

        gridLayout->addWidget(lineEdit_length, 2, 1, 1, 1);

        label_4 = new QLabel(Dialog_Parameters);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 3, 0, 1, 1);

        lineEdit_thickness = new QLineEdit(Dialog_Parameters);
        lineEdit_thickness->setObjectName(QString::fromUtf8("lineEdit_thickness"));

        gridLayout->addWidget(lineEdit_thickness, 1, 1, 1, 1);

        label = new QLabel(Dialog_Parameters);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        lineEdit_gain = new QLineEdit(Dialog_Parameters);
        lineEdit_gain->setObjectName(QString::fromUtf8("lineEdit_gain"));

        gridLayout->addWidget(lineEdit_gain, 6, 1, 1, 1);

        label_7 = new QLabel(Dialog_Parameters);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout->addWidget(label_7, 6, 0, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);


        retranslateUi(Dialog_Parameters);
        QObject::connect(buttonBox, SIGNAL(accepted()), Dialog_Parameters, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Dialog_Parameters, SLOT(reject()));

        comboBox_symmetrize->setCurrentIndex(-1);
        comboBox_forceKxy->setCurrentIndex(-1);


        QMetaObject::connectSlotsByName(Dialog_Parameters);
    } // setupUi

    void retranslateUi(QDialog *Dialog_Parameters)
    {
        Dialog_Parameters->setWindowTitle(QCoreApplication::translate("Dialog_Parameters", "Sample Parameters", nullptr));
        label_6->setText(QCoreApplication::translate("Dialog_Parameters", "Force kxy", nullptr));
        label_2->setText(QCoreApplication::translate("Dialog_Parameters", "Thickness: ", nullptr));
        label_3->setText(QCoreApplication::translate("Dialog_Parameters", "Length: ", nullptr));
        comboBox_symmetrize->setItemText(0, QCoreApplication::translate("Dialog_Parameters", "True", nullptr));
        comboBox_symmetrize->setItemText(1, QCoreApplication::translate("Dialog_Parameters", "False", nullptr));

        comboBox_symmetrize->setCurrentText(QCoreApplication::translate("Dialog_Parameters", "Optional", nullptr));
        comboBox_symmetrize->setPlaceholderText(QCoreApplication::translate("Dialog_Parameters", "Optional", nullptr));
        comboBox_forceKxy->setItemText(0, QCoreApplication::translate("Dialog_Parameters", "False", nullptr));
        comboBox_forceKxy->setItemText(1, QCoreApplication::translate("Dialog_Parameters", "True", nullptr));

        comboBox_forceKxy->setPlaceholderText(QCoreApplication::translate("Dialog_Parameters", "Optional", nullptr));
        lineEdit_width->setText(QCoreApplication::translate("Dialog_Parameters", "1e-6", nullptr));
        label_5->setText(QCoreApplication::translate("Dialog_Parameters", "Symmetrize", nullptr));
        comboBox_sign->setItemText(0, QCoreApplication::translate("Dialog_Parameters", "Positive", nullptr));
        comboBox_sign->setItemText(1, QCoreApplication::translate("Dialog_Parameters", "Negative", nullptr));

        lineEdit_length->setText(QCoreApplication::translate("Dialog_Parameters", "1e-6", nullptr));
        label_4->setText(QCoreApplication::translate("Dialog_Parameters", "Sign: ", nullptr));
        lineEdit_thickness->setText(QCoreApplication::translate("Dialog_Parameters", "1e-6", nullptr));
        label->setText(QCoreApplication::translate("Dialog_Parameters", "Width: ", nullptr));
        lineEdit_gain->setText(QCoreApplication::translate("Dialog_Parameters", "1000", nullptr));
        label_7->setText(QCoreApplication::translate("Dialog_Parameters", "Gain", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog_Parameters: public Ui_Dialog_Parameters {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PARAMETERS_DIALOG_H
