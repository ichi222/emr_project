# 電子カルテ (EMR) アプリ

このアプリは、Django を使用して構築されたシンプルな電子カルテ (EMR) アプリケーションです。患者データの管理、処置の記録、アップロードされた医療画像の表示機能を提供します。このアプリはデモおよび学習目的で設計されています。

---

## 機能

- **患者管理**:
  - 患者情報の追加、表示、更新、削除。
  - 患者データには、名前、生年月日、性別、病歴が含まれます。

- **処置記録**:
  - 患者に関連する処置を記録し、表示。
  - 処置記録は時系列で表示されます。

- **医療画像管理**:
  - 医療画像をアップロードし、患者ごとに表示。

---

## 必要条件

- Python 3.8+
- Django 5.1.4
- SQLite3
- Pillow（画像処理用）

---

## インストール手順

1. このリポジトリをクローンします：
   ```bash
   git clone <repository-url>
   cd emr_project
   ```

2. 仮想環境を作成して有効化します：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

3. 必要な依存関係をインストールします：
   ```bash
   pip install -r requirements.txt
   ```

4. マイグレーションを適用してデータベースをセットアップします：
   ```bash
   python manage.py migrate
   ```

5. スーパーユーザーアカウントを作成します：
   ```bash
   python manage.py createsuperuser
   ```

6. 開発サーバーを起動します：
   ```bash
   python manage.py runserver
   ```

7. ブラウザで以下のURLにアクセスします：
   - メインサイト: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - 管理画面: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ファイル構成

```
emr_project/
├── emr_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── emr/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   ├── emr/
│   │       ├── patient_list.html
│   │       ├── treatment_list.html
│   │       ├── medical_image_list.html
│   ├── urls.py
│   ├── views.py
├── manage.py
├── db.sqlite3
├── media/
│   ├── (アップロードされた画像)
├── requirements.txt
```



---

## 使用方法

1. 管理画面から患者情報を追加します。
2. 各患者に関連する処置を記録し、医療画像をアップロードします。
3. アプリケーション内で患者データと関連記録を管理・表示します。

---

## ライセンス

このプロジェクトは MIT ライセンスの下で提供されています。詳細は `LICENSE` ファイルをご覧ください。


