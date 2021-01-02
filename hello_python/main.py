#! env python
# -*- coding: utf-8 -*-

# ${PROJECT_NAME}.${NAME}
# Date: ${YEAR}/${MONTH}/${DAY}
# Filename: ${NAME}

__author__ = "$USER"
__date__ = "${YEAR}/${MONTH}/${DAY}"


from hello_python.application import Application


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
