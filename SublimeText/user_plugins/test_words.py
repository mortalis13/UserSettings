
# Tests for words lookup, permutations of letters

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno
import http.client
import itertools
import time


class TestWordsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print()
    start = time.time()
    
    self.test()
    print('finish')
    
    end = time.time()
    print('time:', end - start)
  
  
  def test(self):
    letters = 'abcdefg'
    letters = tuple(letters)
    
    words = [
      'def',
      'fab',
      'fsdf',
      'qwee',
      'beag',
    ]
    
    avail = {}
    for c in letters:
      if not c in avail:
        avail[c] = 1;
      else:
        avail[c] += 1;
        
    res = []
    for word in words:
      word = word.strip()
      word_chars = tuple(word)
      
      count = {}
      ok = True
      
      for c in word_chars:
        if not c in count:
          count[c] = 1;
        else:
          count[c] += 1;
          
        if (not c in avail) or (count[c] > avail[c]):
          ok = False
          break
          
      if ok:
        res.append(word)
        
    print(res)
    
    
  def test4(self):
    letters = 'abcd'
    letters = 'askeim'
    letters = 'akeim'
    letters = 'ekspcmatlri'
    letters = 'ekspcmatlr'
    letters = 'xkaiqmorñr'
    letters = 'uñgynefraatte'
    letters = 'upaíajcrwb'
    letters = 'fródnailñof'
    
    exclude_first_letters = ''
    # exclude_first_letters = 'eka'
    # exclude_first_letters = 'spcmtlr'
    # exclude_first_letters = 'xkiqño'
    # exclude_first_letters = 'amrr'
    # exclude_first_letters = 'uñygnfrt'
    
    word_len = len(letters)
    word_len = 8
    
    words = ''
    
    # res = itertools.permutations(letters, word_len)
    res = permutations34(letters, word_len)
    
    for word_array in res:
      if word_array[0] in exclude_first_letters:
        continue
        
      word_array = list(word_array)
      word_array.insert(2, 'h')
      words += ''.join(word_array) + '\n'
    
    sublime.set_clipboard(words)
    
    
  def test3(self):
    letters = 'abcdefghig'
    # letters = 'ekspcmatlri'
    
    word_len = len(letters)
    # word_len = 7
    
    res = itertools.permutations(letters, word_len)
    
    words = ''
    for word_array in res:
      word = ''
      for letter in word_array:
        word += letter
      
      words += word + '\n'
    
    sublime.set_clipboard(words)
          

  def test2(self):
    # letters = 'abcd'
    # letters = 'abcdefghig'
    letters = 'askeim'
    
    words = ''
    
    data = list(letters)
    res = comb(data)
    
    for word_array in res:
      words += ''.join(word_array) + '\n'
      # print(''.join(word_array))
    
    sublime.set_clipboard(words)
    # print(res)
    
    
  def test1(self):
    grid = ['fxie', 'amlo', 'ewbx', 'astu']
    g, c = make_graph(grid)
    
    print(g)
    print(c)
    
    # w, p = make_lookups(grid)
    # res = set()
    # find_words(g, c, None, [], res, w, p)
    
    # print(res)
 

def make_graph(grid):
    root = None
    graph = { root:set() }
    chardict = { root:'' }

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            chardict[(i, j)] = char
            node = (i, j)
            children = set()
            graph[node] = children
            graph[root].add(node)
            add_children(node, children, grid)

    return graph, chardict

def add_children(node, children, grid):
    x0, y0 = node
    for i in [-1,0,1]:
        x = x0 + i
        if not (0 <= x < len(grid)):
            continue
        for j in [-1,0,1]:
            y = y0 + j
            if not (0 <= y < len(grid[0])) or (i == j == 0):
                continue

            children.add((x,y))


def find_words(graph, chardict, position, prefix, results, words, prefixes):
    """ Arguments:
      graph :: mapping (x,y) to set of reachable positions
      chardict :: mapping (x,y) to character
      position :: current position (x,y) -- equals prefix[-1]
      prefix :: list of positions in current string
      results :: set of words found
      words :: set of valid words in the dictionary
      prefixes :: set of valid words or prefixes thereof
    """
    word = to_word(chardict, prefix)

    if word not in prefixes:
        return

    if word in words:
        results.add(word)

    for child in graph[position]:
        if child not in prefix:
            find_words(graph, chardict, child, prefix+[child], results, words, prefixes)


def make_lookups(grid, fn='dict.txt'):
    # Make set of valid characters.
    chars = set()
    for word in grid:
        chars.update(word)

    words = set(x.strip() for x in open(fn) if set(x.strip()) <= chars)
    prefixes = set()
    for w in words:
        for i in range(len(w)+1):
            prefixes.add(w[:i])

    return words, prefixes


def comb(data):
  if len(data) <= 1:
    return [data]
        
  res = []
  
  for i, c in enumerate(data):
    for r in comb(data[:i] + data[i+1:]):
      res.append([c] + r)
  
  return res


def permutations27(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def permutations34(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    
    pool = tuple(iterable)
    
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
        
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
