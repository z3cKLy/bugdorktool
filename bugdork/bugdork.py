#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from googlesearch import search
import time

def load_dorks(filename="dorks.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("⚠️ dorks.txt bulunamadı. Önce dork listesini oluştur!")
        return []

def bug_bounty_dork_scan(target, dorks):
    report_file = f"{target}_rapor.txt"
    with open(report_file, "w", encoding="utf-8") as rapor:
        rapor.write(f"Bug Bounty Dork Taraması - {target}\n")
        rapor.write("="*60 + "\n\n")

        for dork in dorks:
            query = f"site:{target} {dork}"
            print(f"\n[🔍] Arama: {query}\n")
            rapor.write(f"\n[🔍] Arama: {query}\n")

            try:
                for url in search(query, num_results=5, lang="en"):
                    print(f"   -> {url}")
                    rapor.write(f"   -> {url}\n")
                    time.sleep(1)  # ban yememek için bekleme
            except Exception as e:
                print(f"Hata: {e}")
                rapor.write(f"Hata: {e}\n")

            print("-"*60)
            rapor.write("-"*60 + "\n")

    print(f"\n✅ Tarama tamamlandı. Rapor kaydedildi: {report_file}")

if __name__ == "__main__":
    target_site = input("Hedef site adresini gir (örnek: kocamanlarbalik.com): ")
    dork_list = load_dorks("dorks.txt")
    if dork_list:
        bug_bounty_dork_scan(target_site, dork_list)
