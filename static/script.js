document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("fetchButton");
    if (button) {
      button.addEventListener("click", fetchTriples);
    }
  });
  
  async function fetchTriples() {
    const limitInput = document.getElementById("limit");
    const output = document.getElementById("output");
    if (!limitInput || !output) {
      console.error("必要なDOM要素が見つかりません");
      return;
    }
  
    const limit = limitInput.value;
  
    try {
      const response = await fetch(`/triples?limit=${limit}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
  
      // dataが { triples: [...] } の形か、単なる配列か判別
      const triples = Array.isArray(data) ? data : data.triples;
  
      if (!Array.isArray(triples)) {
        throw new Error("レスポンスの形式が不正です");
      }
  
      output.textContent = triples.map(t => `(${t[0]}, ${t[1]}, ${t[2]})`).join('\n');
    } catch (error) {
      console.error("取得に失敗しました:", error);
      output.textContent = "データ取得に失敗しました。コンソールを確認してください。";
    }
  }
  