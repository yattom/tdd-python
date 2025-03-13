/**
 * 自動販売機クラス
 */
class VendingMachine {
  /**
   * コンストラクタ
   * @param {Object} inventory - 初期在庫 { 商品名: { price: 価格, stock: 在庫数 } }
   * @param {number} changeAmount - 初期釣り銭の金額
   */
  constructor(inventory = {}, changeAmount = 0) {
    this.inventory = { ...inventory };
    this.changeAmount = changeAmount;
    this.insertedAmount = 0;
    this.timeoutId = null;
  }

  /**
   * 在庫情報を取得
   * @returns {Object} 在庫情報
   */
  getInventory() {
    return { ...this.inventory };
  }

  /**
   * 特定の商品の在庫情報を設定
   * @param {string} productName - 商品名
   * @param {Object} info - 商品情報 { price: 価格, stock: 在庫数 }
   */
  setInventory(productName, info) {
    this.inventory[productName] = { ...info };
  }

  /**
   * 投入金額を取得
   * @returns {number} 投入金額
   */
  getInsertedAmount() {
    return this.insertedAmount;
  }

  /**
   * お金を投入
   * @param {number} amount - 投入金額
   */
  insertMoney(amount) {
    // 受け付ける硬貨・紙幣：10円、50円、100円、500円、1000円
    const validCoins = [10, 50, 100, 500, 1000];
    
    // 有効な硬貨・紙幣でなければ何もしない
    if (!validCoins.includes(amount)) {
      return;
    }
    
    this.insertedAmount += amount;
    
    // 一定時間後に自動返却するタイマーをリセット
    this._resetAutoReturnTimer();
  }

  /**
   * 商品を購入
   * @param {string} productName - 商品名
   * @returns {Object} 購入結果
   */
  purchase(productName) {
    // タイマーをクリア
    this._clearAutoReturnTimer();
    
    // 商品が存在するか確認
    if (!this.inventory[productName]) {
      const returnedMoney = this.insertedAmount;
      this.insertedAmount = 0;
      return {
        success: false,
        message: '商品が存在しません',
        returnedMoney
      };
    }
    
    const product = this.inventory[productName];
    
    // 在庫があるか確認
    if (product.stock <= 0) {
      const returnedMoney = this.insertedAmount;
      this.insertedAmount = 0;
      return {
        success: false,
        message: '商品は売り切れです',
        returnedMoney
      };
    }
    
    // 投入金額が足りるか確認
    if (this.insertedAmount < product.price) {
      const returnedMoney = this.insertedAmount;
      this.insertedAmount = 0;
      return {
        success: false,
        message: '投入金額が不足しています',
        returnedMoney
      };
    }
    
    // 釣り銭の金額
    const change = this.insertedAmount - product.price;
    
    // 釣り銭が足りるか確認
    if (change > this.changeAmount) {
      const returnedMoney = this.insertedAmount;
      this.insertedAmount = 0;
      return {
        success: false,
        message: '釣り銭が不足しています',
        returnedMoney
      };
    }
    
    // 購入処理
    this.inventory[productName].stock--;
    this.changeAmount += product.price; // 売上を釣り銭に追加
    this.changeAmount -= change; // 釣り銭から返却分を減らす
    this.insertedAmount = 0;
    
    return {
      success: true,
      product: productName,
      change
    };
  }

  /**
   * 投入金額をキャンセル
   * @returns {number} 返却金額
   */
  cancel() {
    this._clearAutoReturnTimer();
    const returnedMoney = this.insertedAmount;
    this.insertedAmount = 0;
    return returnedMoney;
  }

  /**
   * 自動返却タイマーをリセット
   * @private
   */
  _resetAutoReturnTimer() {
    this._clearAutoReturnTimer();
    
    // 30秒後に自動返却
    this.timeoutId = setTimeout(() => {
      this.cancel();
    }, 30000);
  }

  /**
   * 自動返却タイマーをクリア
   * @private
   */
  _clearAutoReturnTimer() {
    if (this.timeoutId) {
      clearTimeout(this.timeoutId);
      this.timeoutId = null;
    }
  }
}

module.exports = VendingMachine;
