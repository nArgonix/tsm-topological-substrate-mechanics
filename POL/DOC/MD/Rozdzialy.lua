-- custom-numbering.lua
function Header(el)
  -- Tylko dla HTML
  if FORMAT:match("html") then
    if el.level == 1 then
      -- Dla rozdziału: "Rozdział 1. Tytuł"
      local num = el.attr.attributes["number"] or pandoc.utils.stringify(el.identifier):match("%d+")
      if not num then num = "" end
      
      local prefix = pandoc.Str("Rozdział " .. num .. ". ")
      el.content = pandoc.Inlines({prefix}) + el.content
    elseif el.level >= 2 then
      -- Dla podrozdziałów: tylko numer (1.1, 1.1.1 itd.)
      local num = el.attr.attributes["number"] or ""
      if num ~= "" then
        local prefix = pandoc.Str(num .. " ")
        el.content = pandoc.Inlines({prefix}) + el.content
      end
    end
  end
  return el
end

return {
  {Header = Header}
}