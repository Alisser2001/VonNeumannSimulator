import { Inter } from "next/font/google";
import "./globals.css";
import { QueryClientProvider } from "@tanstack/react-query";
import queryClient from "./queryClient";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Von Neumann Simulator",
  description: "Von Neumann Simulator",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <QueryClientProvider client={queryClient}>
          {children}
        </QueryClientProvider>
      </body>
    </html>
  );
}
