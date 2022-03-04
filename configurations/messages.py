from aiogram.utils.markdown import bold, text

cancel_message = text(bold("\n\n Для відміни натисніть, або введіть команду /cancel\n"))
skip_message = text(bold("\n\nДля пропуску цього кроку натисніть /skip\n"))
example_info_message = "\n\nПриклад інформації:\nСьогодні о такій то годині я помітив мітку," \
                       " на стіні житлового будинку/побачив групу осіб," \
                       " які поводили себе дивно/випадок розкрадання майна."
welcome_message = text(bold("\n\nСлава Україні! Щоб надати інформацію - натисніть кнопку в меню.\n"))
