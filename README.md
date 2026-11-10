# BasketIQ

![Status](https://img.shields.io/badge/status-early%20development-orange)
![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)

BasketIQ turns your grocery receipts into something you can actually learn from.

Most of us have no idea where the money goes at the supermarket. The information is all there on the receipt, but it ends up crumpled in a pocket. BasketIQ reads those receipts for you and keeps track of what you bought, where, and how much it cost.

## What it does

- **Reads receipts.** Take a photo of a receipt and BasketIQ pulls out the store, the items, the quantities and the prices.
- **Keeps your history.** Every receipt is saved, so your past shopping trips are always one lookup away.
- **Shows where the money goes.** Totals and item prices add up over time, so you can spot what is getting expensive and what you buy more than you think.

## Where it stands

BasketIQ is at the very beginning. Right now the foundation is being laid: the database for receipts and items, the server, and the first experiments with reading receipt images. There is nothing to install or try yet.

## Built with

- Python and FastAPI for the server
- PostgreSQL for storing receipts and items
- OCR and machine learning (PyTorch, OpenCV) for reading receipt photos

## What's next

- Reliable receipt reading from a phone photo
- User accounts
- A simple app to browse your receipts and spending
