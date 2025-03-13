const VendingMachine = require('./vendingMachine');

describe('VendingMachine', () => {
  let vendingMachine;
  
  beforeEach(() => {
    // テスト前に自動販売機を初期化
    const initialInventory = {
      'コーラ': { price: 150, stock: 5 },
      'お茶': { price: 130, stock: 5 },
      '水': { price: 100, stock: 5 }
    };
    const initialChange = 1000; // 初期釣り銭：1000円
    vendingMachine = new VendingMachine(initialInventory, initialChange);
  });
  
  afterEach(() => {
    // タイマーをクリーンアップ
    if (vendingMachine && vendingMachine.timeoutId) {
      clearTimeout(vendingMachine.timeoutId);
    }
    jest.clearAllTimers();
  });

  test('初期状態で正しく在庫と価格が設定されている', () => {
    expect(vendingMachine.getInventory()).toEqual({
      'コーラ': { price: 150, stock: 5 },
      'お茶': { price: 130, stock: 5 },
      '水': { price: 100, stock: 5 }
    });
  });

  describe('お金を投入できる', () => {
    test.each([10, 50, 100, 500, 1000])('正しい金額が投入できる: %i円', (amount) => {
      vendingMachine.insertMoney(amount);
      expect(vendingMachine.getInsertedAmount()).toBe(amount);
    });
    
    test('複数のお金を投入できる', () => {
      vendingMachine.insertMoney(100);
      vendingMachine.insertMoney(50);
      expect(vendingMachine.getInsertedAmount()).toBe(150);
    });

    test('有効なお金以外は投入できない', () => {
      vendingMachine.insertMoney(1);
      expect(vendingMachine.getInsertedAmount()).toBe(0);
    });
  });

  describe('投入金額が足りる場合、商品を購入できる', () =>{
    test('正しく購入できる', () => {
      vendingMachine.insertMoney(100);
      vendingMachine.insertMoney(100);
      const result = vendingMachine.purchase('コーラ');
      
      expect(result.success).toBe(true);
      expect(result.product).toBe('コーラ');
      expect(vendingMachine.getInsertedAmount()).toBe(0); // 投入金額がリセット
    });
    test('購入後は投入金額がリセットされる', () => {
      vendingMachine.insertMoney(100);
      vendingMachine.insertMoney(100);
      const result = vendingMachine.purchase('コーラ');
      
      expect(vendingMachine.getInsertedAmount()).toBe(0); // 投入金額がリセット
    });
    test('お釣りがある', () => {
      vendingMachine.insertMoney(100);
      vendingMachine.insertMoney(100);
      const result = vendingMachine.purchase('コーラ');
      
      expect(result.change).toBe(50); // 200円 - 150円 = 50円のお釣り
    });
    test('お釣りがない', () => {
      vendingMachine.insertMoney(50);
      vendingMachine.insertMoney(100);
      const result = vendingMachine.purchase('コーラ');
      
      expect(result.change).toBe(0);
    });
    test('購入できると在庫が減る', () => {
      vendingMachine.insertMoney(50);
      vendingMachine.insertMoney(100);
      const result = vendingMachine.purchase('コーラ');
      
      expect(vendingMachine.getInventory()['コーラ'].stock).toBe(4); // 在庫が減少
    });
  });
  
  describe('投入金額が足りない場合、商品を購入できない', () => {
    test('商品が出ない', () => {
      vendingMachine.insertMoney(100);
      const result = vendingMachine.purchase('コーラ');
      
      expect(result.success).toBe(false);
      expect(result.message).toBe('投入金額が不足しています');
      expect(result.returnedMoney).toBe(100); // 投入金額が返却される
      expect(vendingMachine.getInsertedAmount()).toBe(0); // 投入金額がリセット
    });
    test('在庫が減らない', () => {
      vendingMachine.insertMoney(100);
      const result = vendingMachine.purchase('コーラ');
      
      expect(vendingMachine.getInventory()['コーラ'].stock).toBe(5); // 在庫は減少しない
    });
  });

  test('商品が売り切れの場合、購入できない', () => {
    // 在庫を0に設定
    vendingMachine.setInventory('コーラ', { price: 150, stock: 0 });
    
    vendingMachine.insertMoney(100);
    vendingMachine.insertMoney(100);
    const result = vendingMachine.purchase('コーラ');
    
    expect(result.success).toBe(false);
    expect(result.message).toBe('商品は売り切れです');
    expect(result.returnedMoney).toBe(200); // 投入金額が返却される
    expect(vendingMachine.getInsertedAmount()).toBe(0); // 投入金額がリセット
  });

  test('釣り銭が不足している場合、商品を購入できない', () => {
    // 釣り銭を少なく設定
    vendingMachine = new VendingMachine({
      'コーラ': { price: 150, stock: 5 }
    }, 40); // 釣り銭が40円しかない
    
    vendingMachine.insertMoney(100);
    vendingMachine.insertMoney(100);
    const result = vendingMachine.purchase('コーラ');
    
    expect(result.success).toBe(false);
    expect(result.message).toBe('釣り銭が不足しています');
    expect(result.returnedMoney).toBe(200); // 投入金額が返却される
    expect(vendingMachine.getInsertedAmount()).toBe(0); // 投入金額がリセット
  });

  test('投入金額をキャンセルできる', () => {
    vendingMachine.insertMoney(100);
    vendingMachine.insertMoney(50);
    
    const returnedMoney = vendingMachine.cancel();
    
    expect(returnedMoney).toBe(150);
    expect(vendingMachine.getInsertedAmount()).toBe(0);
  });

  test('一定時間後に自動的に投入金額が返却される', () => {
    jest.useFakeTimers();
    
    vendingMachine.insertMoney(100);
    expect(vendingMachine.getInsertedAmount()).toBe(100);
    
    // 30秒経過
    jest.advanceTimersByTime(30000);
    
    expect(vendingMachine.getInsertedAmount()).toBe(0);
    
    jest.useRealTimers();
  });
});
